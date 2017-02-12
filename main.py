#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import ceasar
import cgi

class MainHandler(webapp2.RequestHandler):

    def get(self):
        header = "<h2>Web Caesar</h2>"
        rot_label = "<label>Rotate by: </label>"
        message_label = "<label>Type a message:</label>"

        rotation_input = "<input type='number' name='rotation' />"
        textarea = "<textarea name='message'>" "</textarea>"
        submit = "<input type='submit'></input>"

        form = ("<form method='post'>" + message_label + "<br>" +
        textarea + "<br>" + "<br>" + rot_label + rotation_input +
        "<br>" + "<br>" + submit + "</form>")

        self.response.write(header + form)

    def post(self):
        message = self.request.get("message")
        escaped_message = cgi.escape(message)
        rotation = int(self.request.get("rotation"))
        encrypted_message = ceasar.encrypt(escaped_message, rotation)

        header = "<h2>Web Caesar</h2>"

        rot_label = "<label>Rotate by: </label>"
        message_label = "<label>Type a message:</label>"

        rotation_input = "<input type='number' name='rotation' />"
        textarea = "<textarea name='message'>" + encrypted_message + "</textarea>"
        submit = "<input type='submit'></input>"

        form = ("<form method='post'>" + message_label + "<br>" +
        textarea + "<br>" + "<br>" + rot_label + rotation_input +
        "<br>" + "<br>" + submit + "</form>")

        self.response.write(header + form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
