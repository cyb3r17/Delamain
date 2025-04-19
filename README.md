# Delamain
A tiny project I made over the weekend to see how autonomous driving would look with linear regression.

Inspired by [navlab](https://en.wikipedia.org/wiki/Navlab) .

## How it works
- A script `data_capture.py` takes a screenshot of the screen every second (particularly the car area) (feature, X)
- Maps my key presses to the image
- Key press can be defined as throttle, steering, and brake (though the break part is kinda useless for now) (label, Y)
- apply linear regression to this data after flattening said images
- profit ???

## License
MIT License, feel free to contribute or improve (i'm always learning :D)
