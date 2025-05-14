# FoldableGroup

## Overview
A group of foldable containers that doesn't allow more than one container to be expanded at a time.

## Description
A group of FoldableContainer-derived nodes. Only one container can be expanded at a time.

## Properties
- **allow_folding_all**: `bool` = `false`  
  If true, it is possible to fold all containers in this FoldableGroup.
- **resource_local_to_scene**: `bool` = `true`  
  Overrides Resource property resource_local_to_scene.

## Methods
- **get_containers()** → `Array[FoldableContainer]`  
  Returns an array of FoldableContainer instances that have this as their FoldableGroup.
- **get_expanded_container()** → `FoldableContainer`  
  Returns the current expanded container.

## Signals
- **expanded(container: FoldableContainer)**  
  Emitted when one of the containers of the group is expanded.

## Property Descriptions
- **allow_folding_all**: `bool` = `false`  
  If true, it is possible to fold all containers in this FoldableGroup.

## Method Descriptions
- **get_containers()** → `Array[FoldableContainer]`  
  Returns an array of FoldableContainer instances that have this as their FoldableGroup (see FoldableContainer.foldable_group).
- **get_expanded_container()** → `FoldableContainer`  
  Returns the current expanded container.