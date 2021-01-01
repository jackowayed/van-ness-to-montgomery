# Van Ness to Montgomery

This app uses the Nextbus API to give a picture of the health of
the SF Muni subway.

It tracks the most recent trains that have traveled from Van Ness to Montgomery
and how long it took them, to give a picture of subway congestion and other issues.

In addition, it shows upcoming trains.

## Deployment

To deploy, run as a single Python process and setup a crontab that requests
/update-times (POST) every ~30 seconds.

## Known Limitations

Given that the storage of the times is in process, this cannot be scaled up
to multiple processes, and it will fully start from scratch if the process is
restarted.

I have never in pr

There is also no pruning of the times deque. This impacts RAM usage but not runtime.
Empirically, this hasn't been a problem even running it on Glitch for months;
I haven't looked closely at whether Glitch is restarting it from time to time,
but there's only ~200 train runs a day, so that's only ~60k/year, so we're talking about
~1MB if it ever gets