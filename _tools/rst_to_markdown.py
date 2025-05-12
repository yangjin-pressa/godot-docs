import re
import os
from argparse import ArgumentParser
from os.path import isfile, isdir, join, basename, splitext, dirname


def parse_and_get_arguments():
    """Creates and returns an object with parsed arguments."""
    parser = ArgumentParser(
        prog="rst_to_markdown",
        description="Converts reStructuredText files to Markdown format.",
    )
    parser.add_argument(
        "-f", "--files", nargs="*", help="Paths of specific RST documents to convert.",
    )
    parser.add_argument(
        "-d", "--directory", help="Path to directory containing RST files to convert (processes all .rst files)."
    )
    parser.add_argument(
        "-o", "--output_dir", required=True, help="Path to the output directory for converted files.",
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true", help="Recursively process subdirectories when using --directory option."
    )
    return parser.parse_args()


def find_rst_files(directory, recursive=False):
    """Find all .rst files in the given directory."""
    rst_files = []
    
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.rst'):
                    rst_files.append(join(root, file))
    else:
        for file in os.listdir(directory):
            file_path = join(directory, file)
            if isfile(file_path) and file.endswith('.rst'):
                rst_files.append(file_path)
                
    return rst_files


def convert_heading(line, next_line=None):
    """Convert RST-style headings to Markdown-style headings."""
    if next_line and re.match(r'^[=]+$', next_line):
        return f"# {line}\n"
    elif next_line and re.match(r'^[-]+$', next_line):
        return f"## {line}\n"
    elif next_line and re.match(r'^[~]+$', next_line):
        return f"### {line}\n"
    elif next_line and re.match(r'^[`]+$', next_line):
        return f"#### {line}\n"
    elif next_line and re.match(r'^[\']+$', next_line):
        return f"##### {line}\n"
    elif next_line and re.match(r'^[\.]+$', next_line):
        return f"###### {line}\n"
    return line + "\n"


def convert_code_block(lines, i):
    """Convert RST code blocks to Markdown code blocks."""
    if not re.match(r'\.\. code-block::(.*)', lines[i]):
        return None, i
    
    language = re.match(r'\.\. code-block::(.*)', lines[i])
    language = language.group(1).strip() if language else ""
    
    result = f"```{language}\n"
    i += 1
    
    # Skip any blank lines or indentation specifiers
    while i < len(lines) and (not lines[i].strip() or re.match(r'\s+:.*:', lines[i])):
        i += 1
    
    # Get the code block content
    indent = None
    while i < len(lines):
        if not lines[i].strip():
            result += "\n"
            i += 1
            continue
        
        # Detect indentation of the first line of the code block
        if indent is None:
            match = re.match(r'(\s+)', lines[i])
            if match:
                indent = len(match.group(1))
            else:
                indent = 0
        
        # Check if we're still in the code block
        current_indent = len(re.match(r'(\s*)', lines[i]).group(1))
        if current_indent < indent:
            break
        
        # Add the line to the result, removing the indent
        result += lines[i][indent:] + "\n"
        i += 1
    
    result += "```\n"
    return result, i - 1  # Return the last processed line index


def convert_list_item(line):
    """Convert RST list items to Markdown list items."""
    if re.match(r'\*\s+', line):
        return line  # Both use * for unordered lists
    elif re.match(r'#\.\s+', line):
        return re.sub(r'#\.(\s+)', r'1.\1', line)  # Convert #. to 1.
    elif re.match(r'\d+\.\s+', line):
        return line  # Both use 1. for ordered lists
    return line


def convert_image(line):
    """Convert RST image directives to Markdown image syntax."""
    match = re.match(r'\.\. image::\s+(.*)', line)
    if match:
        image_path = match.group(1).strip()
        return f"![Image]({image_path})\n"
    return line + "\n"


def convert_link(text):
    """Convert RST-style links to Markdown-style links."""
    # Convert `Link text <URL>`_ to [Link text](URL)
    text = re.sub(r'`([^`<]+)\s+<([^>]+)>`_', r'[\1](\2)', text)
    return text


def convert_rst_to_markdown(rst_content):
    """Convert RST content to Markdown."""
    lines = rst_content.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Handle headings
        if i < len(lines) - 1:
            heading_result = convert_heading(line, lines[i + 1])
            if heading_result != line + "\n":
                result.append(heading_result)
                i += 2  # Skip the heading underline
                continue
        
        # Handle code blocks
        code_block_result, new_i = convert_code_block(lines, i)
        if code_block_result:
            result.append(code_block_result)
            i = new_i + 1
            continue
        
        # Handle images
        if re.match(r'\.\. image::', line):
            result.append(convert_image(line))
            i += 1
            continue
        
        # Handle list items
        line = convert_list_item(line)
        
        # Handle links
        line = convert_link(line)
        
        # Remove RST directives
        if re.match(r'\.\.\s+\w+::', line):
            i += 1
            continue
        
        result.append(line + "\n")
        i += 1
    
    return ''.join(result)


def copy_images_for_document(doc_path, output_dir):
    """Copy images referenced in the RST file to the output directory."""
    image_dir = dirname(doc_path)
    image_paths = []
    
    try:
        with open(doc_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                match = re.match(r'\.\. image::\s+(.*)', line)
                if match:
                    image_path = match.group(1).strip()
                    src_image_path = join(image_dir, image_path)
                    image_paths.append((src_image_path, image_path))
    except Exception as e:
        print(f"Error reading file for image references {doc_path}: {e}")
    
    for src_image_path, rel_image_path in image_paths:
        if isfile(src_image_path):
            # Create image directory structure in output_dir
            dest_img_dir = join(output_dir, dirname(rel_image_path))
            if not isdir(dest_img_dir):
                os.makedirs(dest_img_dir, exist_ok=True)
            dest_image_path = join(output_dir, rel_image_path)
            
            # Copy the image file
            try:
                import shutil
                shutil.copy2(src_image_path, dest_image_path)
                print(f"  Copied image: {rel_image_path}")
            except Exception as e:
                print(f"  Error copying image {src_image_path}: {e}")
        else:
            print(f"  Warning: Referenced image not found: {src_image_path}")


def process_rst_files(documents, output_dir):
    """Process RST files and convert them to Markdown."""
    if not isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    for doc_path in documents:
        if not isfile(doc_path) or not doc_path.endswith('.rst'):
            print(f"Skipping {doc_path}: Not a .rst file")
            continue
        
        try:
            print(f"Converting {doc_path}...")
            with open(doc_path, 'r', encoding='utf-8') as f:
                rst_content = f.read()
            
            md_content = convert_rst_to_markdown(rst_content)
            
            # Preserve directory structure in output
            rel_path = os.path.relpath(doc_path, os.path.commonprefix([os.path.dirname(doc) for doc in documents]))
            rel_dir = os.path.dirname(rel_path)
            
            # Create output directory structure
            target_dir = join(output_dir, rel_dir)
            os.makedirs(target_dir, exist_ok=True)
            
            # Generate output file path
            md_filename = splitext(basename(doc_path))[0] + '.md'
            output_path = join(target_dir, md_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            print(f"  Converted to {output_path}")
            
            # Process and copy images
            copy_images_for_document(doc_path, target_dir)
            
        except Exception as e:
            print(f"  Error processing {doc_path}: {e}")


if __name__ == "__main__":
    args = parse_and_get_arguments()
    
    if not args.output_dir:
        print("Error: Output directory is required.")
        exit(1)
    
    documents = []
    
    # Handle specific files
    if args.files:
        documents.extend([path for path in args.files if path.endswith('.rst')])
    
    # Handle directory
    if args.directory:
        if not isdir(args.directory):
            print(f"Error: Directory not found: {args.directory}")
            exit(1)
        
        documents.extend(find_rst_files(args.directory, args.recursive))
    
    if not documents:
        print("No valid .rst files found to process.")
    else:
        print(f"Found {len(documents)} RST files to convert.")
        process_rst_files(documents, args.output_dir)
        print("Conversion complete!")