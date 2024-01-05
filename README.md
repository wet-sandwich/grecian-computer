# Grecian Computer Solver

## Intro
This code solves the [Grecian Computer](https://projectgeniusinc.com/grecian-computer/).

The puzzle is made of five wooden disks of various sizes and shapes. All disks combined
form four rings of twelve numbers. The puzzle is solved by finding the combination of
rotations of each disk that leads to each radial (column of four numbers) to add up to 42.

## Representing the Puzzle
Each disk is represented as a 4x12 matrix (a list of lists in python). The starting position
of each disk was chosen by finding the smallest number on the outer most ring of that disk.
A zero is used to represent a missing part of a disk where a number would normally be printed.
The bottom disk serves as a reference point for the rotations of all the other disks. Disk
rotations are counter-clockwise.
