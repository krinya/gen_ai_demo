#!/usr/bin/env python3
"""
Test script to demonstrate the chatbot's conversation memory functionality
"""

import asyncio
import sys
sys.path.append('.')

from template_main import create_chatbot

async def test_conversation_memory():
    """Test that the chatbot remembers previous conversation"""
    print("🤖 Testing Conversation Memory\n")
    
    # Create a chatbot instance
    chatbot = await create_chatbot()
    print(f"Session ID: {chatbot.session_id}\n")
    
    # First message
    print("👤 User: What is CleanGo?")
    response1 = await chatbot.chat("What is CleanGo?")
    print(f"🤖 Bot: {response1[:100]}...\n")
    
    # Second message that references the first
    print("👤 User: How much does it cost?")
    response2 = await chatbot.chat("How much does it cost?")
    print(f"🤖 Bot: {response2[:150]}...\n")
    
    # Third message testing memory
    print("👤 User: Can you remind me what we were talking about?")
    response3 = await chatbot.chat("Can you remind me what we were talking about?")
    print(f"🤖 Bot: {response3}\n")
    
    # Show conversation history
    print("📜 Conversation History:")
    history = chatbot.get_conversation_history()
    for i, msg in enumerate(history, 1):
        msg_type = "👤 User" if msg.__class__.__name__ == "HumanMessage" else "🤖 Bot"
        print(f"{i}. {msg_type}: {msg.content[:80]}...")
    
    print(f"\nTotal messages in history: {len(history)}")
    
    # Test reset functionality
    print("\n🔄 Resetting conversation...")
    chatbot.reset_conversation()
    print(f"New session ID: {chatbot.session_id}")
    
    # Test after reset
    history_after_reset = chatbot.get_conversation_history()
    print(f"Messages after reset: {len(history_after_reset)}")

if __name__ == "__main__":
    asyncio.run(test_conversation_memory())
