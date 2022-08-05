# Troubleshooting

This documents some common issues that folks have run into with the examples in this repository. A huge thank you to all those who have contributed both with issues and fixes!

## port 5000 in use by airplay receiver 

> Port 5000 is now in use by airplay receiver in this version of MacOS. One can only assume nobody at Apple uses Flask?
> 
> The easiest fix is to use a different port. However, you can also go into the sharing systems preference and uncheck the airplay receiver.
> More detail here: https://medium.com/pythonistas/port-5000-already-in-use-macos-monterey-issue-d86b02edd36c

#### *originally reported by [@qdzlug] in [#18]*

[@qdzlug]: https://github.com/qdzlug
[#18]: https://github.com/PacktPublishing/Cloud-Native-Observability/issues/18