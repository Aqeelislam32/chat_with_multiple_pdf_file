css = '''
<style>

 
/* مکمل ایپ کا بیک گراؤنڈ */
.stApp {
    background-color: #87CEEB !important; /* Sky Blue */
}

/* سائیڈبار کا رنگ */
[data-testid="stSidebar"] .block-container {
    background-color: #808080 !important; /* Grey */
    padding: 1rem;
}

/* ان پٹ بار کا سبز رنگ */
.stTextInput>div>div>input {
    background-color: #90EE90 !important; /* Light Green */
}

/* سبمٹ بٹن (براؤن) */
.stButton>button {
    background-color: #A52A2A !important; /* Brown */
    color: white !important;
}

/* کلئیر چیٹ بٹن (اورنج) */
.clear-btn {
    background-color:  #A52A2A !important; /* Orange */
    color: white !important;
}

/* styles.css */
h1[data-testid="stMarkdownContainer"] {
        color: #2c3e50 !important;
        font-size: 2.5rem !important;
        text-align: center !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2) !important;
        padding: 1rem !important;
        border-bottom: 3px solid #3498db !important;
    }
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''










bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.pinimg.com/originals/0c/67/5a/0c675a8e1061478d2b7b21b330093444.gif"   >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
#style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;"

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/OIP.uDqZFTOXkEWF9PPDHLCntAHaHa?pid=ImgDet&rs=1">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
