#!/usr/bin/python

# Copyright 2016 dataJAR Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import CoreFoundation

domain = 'com.apple.appstore'
key = 'restrict-store-require-admin-to-install'

key_value = CoreFoundation.CFPreferencesCopyAppValue(key, domain)
print 'Key Value = ', key_value

key_forced = CoreFoundation.CFPreferencesAppValueIsForced(key, domain) 
print 'Key Forced = ', key_forced
