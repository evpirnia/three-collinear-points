# three-collinear-points

Given a CSV with a list of points, determine which points are collinear and print the lines that have at least three collinear points.

## Example

Given the following list of points:

```CSV
0.0,0.0
1.1,1.1
3.5,4.5
2.2,2.2
0.1,1.0
2.1,1.2
3.1,1.3
```

The expected output would be:

```CSV
1,0.0,0.0,1.1,1.1,2.2,2.2
2,1.1,1.1,0.1,1.0,2.1,1.2,3.1,1.3
```

## Run

To run, enter the following command:

```bash
> python main.py -i $INPUT_FILENAME -o $OUTPUT_FILENAME
```

If -o is not specified, then the output filename will default to "output.csv".
