# IIT Online Downloader
Download your IIT online classes with this simple python script.

## Notice

```
PLEASE NOTE I CAN NOT PASTE ANY EXAMPLE URLS DO TO LEGAL REASONS. 
USE AT YOUR OWN RISK AND BE MINDFUL OF COPYRIGHT LAWS. 
THIS WAS DONE FOR PERSONAL USE FOR CLASSES I PAID FOR. 
ONCE AGAIN I DO NOT CONDONE PIRACY AND AM NOT RESPONSIBLE FOR ANYTHING UNLAWFUL WHILE USING THIS SCRIPT. 
THIS IS FOR PERSONAL USE ONLY FOR WHICH YOU HAVE PAID FOR THE CLASS.
```

## Usage
Install python2 and run the program as `python iit_video_dll.py`

A prompt will ask you to type/paste in your iit online class url found in black board. 
*Note: please remove the index.html at the end*. 
It'll then ask you to verify the url. 
Then enter video resolution (720p, 480p or 360p). 
After that it will show you which lecture it's downloading with its current progress.

## Limitations
* Assumes you enter correct base url for the class without index.html at the end
* Assumption is that every lecture has 360p, 480p, and 720p video resolutions.
* Videos will stored in the directory the script is ran in

## Future Improvements
* Make the download of lectures be parallel
* Check if file has been already downladed
    - Verify its been fully downloaded
* Provide the ability to download to a specified directory
    - e.g. CS100 lecures will stored in <specified directory>/CS100
* Make it py2/3 compatible
