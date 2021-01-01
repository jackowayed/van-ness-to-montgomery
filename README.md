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

I have never in practice seen this be an issue other than during development,
when Glitch restarts it every time code is changed.

There is also no pruning of the times deque. This impacts RAM usage but not runtime.
Empirically, this hasn't been a problem even running it on Glitch for months;
There's only hundreds of train runs a day, so that's maybe 100k/year, so a year's
data is a few MB.