from django.shortcuts import render, get_object_or_404, redirect 
from .models import Conversation
from item.models import Item
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:     # here the owner will not have access to this point.
         return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
         return redirect('conversation:detail', pk=conversations.first().id) # rediect to conversation
    
    # here is checked if the conversation is submitted
    if request.method == 'POST':
         
         form = ConversationMessageForm(request.POST)
         if form.is_valid():
              #here we can create a new conversation
              conversation = Conversation.objects.create(item=item)
              # now we need to add the owner and members to the member list
              conversation.members.add(request.user)
              conversation.members.add(item.created_by)
              conversation.save()

              # here below is to create the conversation message.
              conversation_message = form.save(commit=False)
              # now to set a reference to the conversation
              conversation_message.conversation = conversation
              conversation_message.created_by = request.user
              conversation_message.save()

              return redirect('item:detail', pk=item_pk)
         else:
            form = ConversationMessageForm()

         return render(request, 'conversation/news.html', {'form': form})


login_required
def inbox(request):
     conversations = Conversation.objects.filter(members__in=[request.user.id])

     return render(request, 'conversation/inbox.html', {'conversations': conversations})


@login_required
def detail(request, pk):
     conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

     if request.method == 'POST':
          form = ConversationMessageForm(request.POST)
          if form.is_valid():    # Then we can create a new conversation message.
               conversation_message = form.save(commit=False)
               conversation_message.conversation = conversation
               conversation_message.created_by.request.user
               conversation_message.save()

               conversation.save()

               return redirect('conversation:detail', pk=pk)
     else:
          form = ConversationMessageForm()     

     return render(request, 'conversation/details.html', {
          'conversation': conversation,
          'form': form,
     })

