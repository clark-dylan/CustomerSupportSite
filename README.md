Implementation
1. Outcomes
1.1 Source Code

1.2 Supplementary Documentation

Software requirements:
●	Elasticsearch 5.6.7
●	Python 3.6.3
●	Django 1.11.7

		Step-by-step installation:
1.	Download Python 3.6.3. Make sure environment variables are set for both Python and python/scripts
2.	Go into CMD and type in: pip install Django==1.11.7
3.	Please do the following as we need to install various packages after Django has been installed:
a.	pip install django-tinymce4-lite
b.	pip install django-filebrowser-no-grappelli
c.	pip install pillow
d.	pip install django-import-export
e.	pip install django chatterbot
f.	pip install elasticsearch-dsl
4.	After all that has been installed, data needs to be indexed to Elasticsearch. In order to do a one time full index, do the following in the CMD in the project folder:
a.	python manage.py shell
b.	Type in this: from elasticsearchapp.search import *
c.	Then do: bulk_indexing()
d.	Data should now be in Elasticsearch
5.	Run Elasticsearch by going doing elasticsearch-5.6.7/bin/elasticsearch 
6.	Once Elasticsearch is ready, let’s train the chatbot. Do the following in CMD in the project folder: python manage.py train.
7.	Once training is complete, the project is good to go. Run python manage.py runserver
8.	Go to http://127.0.0.1:8000/ and you should see the project
9.	You may want to add your own conversation list for the chatbot. If so, go the place where you installed Python. For example: C:\python3.6.3\Lib\site-packages\chatterbot_corpus\data\english in this folder use the other files as a reference on how to structure your conversation list. Afterwards, go back to your project folder in the CMD and do python manage.py train. The bot is now trained for your conversation lists.


2. Potential Future Functions
●	Live chat: A chatting interface that connects users to live administrators and representatives.
●	Report question/answer: A dropdown function that lets a user report spam, hateful, etc. messages.
●	Naive Bayes filter: A filter that will check what the user wrote upon submission. It will check if it is spam, hate speech, etc. The dataset to train this filter classifier will be based on the pool of finalized reported messages. 
●	Infinite feed: Instead of having the forum being paginated. We can make it so that when the user reaches a certain point, new questions will be loaded automatically that way they just scroll and see more questions.
