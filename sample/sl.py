import slack_sdk

stoken = 'xoxb-5060008758977-5047395059074-uxWRo9uD2Zdw622O5MpVZqcn'
schannel = 'C051ACXGBQD'

def Msg_bot(msg):
    client = slack_sdk.WebClient(token=stoken)
    client.chat_postMessage(channel=schannel, text=msg)

chat = "Test"

Msg_bot(chat)