telnetsrvlib
============

Telnet server using gevent

Copied from http://pytelnetsrvlib.sourceforge.net/
Licensed under the LGPL, as per the SourceForge notes.

telnetsrvlib-green requires gevent to function.

The original telnetsrvlib uses a separate thread to process the input buffer and
semaphores reading and writing - as well as a few sleeps sprinkled here and there.

Added a class function to make it easy to use with a gevent StreamServer:

> server = gevent.server.StreamServer((TELNET_IP_BINDING, TELNET_PORT_BINDING), TelnetHandler.streamserver_handle)
> server.serve_forever()


# To Use #

Import the TelnetHandler, then subclass it to add your own commands.  Your command
will be a class method that starts with cmd and is followed by your command in all caps.
> def cmdECHO(self, params):

The params is a list containing any additional parameters passed to your command.

The docstring is used for generating the console help information, and must be formatted
with at least 3 lines:

 * Line 0:  Command paramater(s) if any. (Can be blank line)
 * Line 1:  Short descriptive text. (Mandatory)
 * Line 2+: Long descriptive text. (Can be blank line)

To write to the console output, use:
 
 * self.writeline( TEXT ) 
 * self.write( TEXT )

You can check the connected terminal type via self.TERM


# Commonly Overridden Items #


 * logger
    ** Default: logger

 * PROMPT
    ** Default: "Telnet Server> "
     
 * WELCOME
    ** Displayed after a successful connection, 
     after the username/password is accepted, 
     if configured.
    ** Default: "You have connected to the telnet server."
     
 * authCallback(self, username, password) 
    ** Reference to authentication function. If
     there is none, no un/pw is requested. Should
     raise an exception if authentication fails
    ** Default: None

 * authNeedUser 
    ** Should a username be requested?
    ** Default: False

 * authNeedPass
    ** Should a password be requested?
    ** Default: False


# Example #

    from telnetsrvlib-green import TelnetHandler
     
    class MyTelnetHandler(TelnetHandler):
        PROMPT = "MyTelnet> "
        WELCOME = "Welcome to my server."
        logging = my_special_logger
        
        def cmdECHO(self, params):
            '''<text to echo>
            Echo text back to the console.
            
            '''
            self.writeline( ' '.join(params) )
        
