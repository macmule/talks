# MacDeployment2021
Repo for links from the MacDeployment 2021 talk "Administering Apple Silicon"

## macOS Big Sur and Apple Silicon
- [macOS Big Sur and Apple Silicon](https://datajar.co.uk/datajar-tech-series-whats-new-with-macos-big-sur-and-apple-silicon/)

## Serial Number Format Changes
- [Apple Plans to Switch to Randomized Serial Numbers for Future Products Starting in 2021](https://www.macrumors.com/2020/01/06/apple-randomized-serial-numbers-late-2020/)
- [Apple Tweaks Serial Number Format With New MacBook Pro](https://www.macrumors.com/2010/04/16/apple-tweaks-serial-number-format-with-new-macbook-pro/)
- [MDM Me Maybe: Device Enrollment Program Security](https://duo.com/labs/research/mdm-me-maybe)

## iOS and iPadOS Apps
- [iOS and iPadOS Apps](https://developer.apple.com/macos/iphone-and-ipad-apps/)

## Rosetta 2
- [If you need to install Rosetta on your Mac](https://support.apple.com/en-gb/HT211861)
- [Installing Rosetta 2 on Apple Silicon Macs](https://derflounder.wordpress.com/2020/11/17/installing-rosetta-2-on-apple-silicon-macs/)
- [Do Adobe apps work on Apple computers that use the M1 chip?](https://helpx.adobe.com/download-install/kb/apple-silicon-m1-chip.html)
- [Deploy Adobe Applications to Apple Silicon Devices](https://dazwallace.wordpress.com/2021/02/06/deploy-adobe-applications-to-apple-silicon-devices/)
- [Platform Support in macOS Installer Packages (pkg)](https://scriptingosx.com/2020/12/platform-support-in-macos-installer-packages-pkg/)

## Apple Configurator 2
- [Revive or restore a Mac with Apple silicon with Apple Configurator 2](https://support.apple.com/en-gb/guide/apple-configurator-2/apdd5f3c75ad/mac)

## madcOS Recovery
- [Boot modes for a Mac with Apple silicon](https://support.apple.com/en-gb/guide/security/sec10869885b/web)
- [Use macOS Recovery on a Mac with Apple silicon](https://support.apple.com/en-gb/guide/mac-help/mchl82829c17/mac)

## Unified Login
Commands to toggle FV2 login screen, `true` to show username and password, `false` to show list of users. Changes should show on restart:
```
sudo defaults write /Library/Preferences/com.apple.loginwindow SHOWFULLNAME -bool true

sudo diskutil ap updatePreboot /
```
- [FileVault login screen differences between Intel and Apple Silicon Macs](https://derflounder.wordpress.com/2021/01/17/filevault-login-screen-differences-between-intel-and-apple-silicon-macs/)

## Firmware Passwords
 - [Set a firmware password on your Mac](https://support.apple.com/en-gb/HT204455)

## Volume Ownership
- [LocalPolicy signing-key creation and management](https://support.apple.com/en-gb/guide/security/sec1f90fbad1/web)
- [Contents of a LocalPolicy file for a Mac with Apple silicon](https://support.apple.com/en-gb/guide/security/secc745a0845/web)

## Startup Security Policy
- [Startup security in macOS](https://support.apple.com/en-gb/guide/deployment-reference-macos/ior2b1833593/web)

## System Extensions
- [Kernel extensions in macOS](https://support.apple.com/en-gb/guide/deployment-reference-macos/apd37565d329/web)
- [Enterprise management of legacy system extensions in macOS Big Sur](https://support.apple.com/en-gb/HT211860)
- [Manage Legacy Kernel Extensions in macOS 11 Using Jamf Pro](https://www.jamf.com/jamf-nation/articles/793/manage-legacy-kernel-extensions-in-macos-11-using-jamf-pro)

## External Startup Disks
- [M1 Macs running Big Sur 11.4 support external disks fully](https://eclecticlight.co/2021/05/27/m1-macs-running-big-sur-11-4-support-external-disks-fully/)

## Mac Sharing Mode
- [Transfer files between a Mac with Apple silicon and another Mac](https://support.apple.com/en-gb/guide/mac-help/mchlb37e8ca7/mac)
