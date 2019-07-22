# slack-link-grabber
Provides a method to use a slash command in Slack and grab a meaningful link.

******

Requires python 3 and the connexion, dotenv and connexion[swagger-ui] modules to be installed. Set a
file in the root directory called `.env` and put two variables in there in the 
following format:

    VERIFICATION_TOKEN=insertTokenHere
    BASE_URL=https://yourURLhere.com/

The token is what your Slack integration provides for use, and the URL is what
you want tacked on the front of the text being sent out.
