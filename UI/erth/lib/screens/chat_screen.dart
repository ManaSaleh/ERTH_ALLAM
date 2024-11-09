import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:erth/constants/constants.dart';
import 'package:erth/models/chat_model.dart';
import 'package:erth/services/api_services.dart';
import 'package:erth/services/assets_manager.dart';
import 'package:erth/widgets/chat_widget.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  bool _isTyping = false;
  late TextEditingController textEditingController;
  late ScrollController _listScrollController;
  late FocusNode focusNode;

  @override
  void initState() {
    _listScrollController = ScrollController();
    textEditingController = TextEditingController();
    focusNode = FocusNode();
    super.initState();
  }

  @override
  void dispose() {
    _listScrollController.dispose();
    textEditingController.dispose();
    focusNode.dispose();
    super.dispose();
  }

  List<ChatModel> chatList = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 2,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Text(
              'الإمام محمد بن سعود',
              textDirection: TextDirection.rtl,
              textAlign: TextAlign.right,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.all(4),
            child: Image.asset(AssetsManager.chatPath),
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            Flexible(
              child: ListView.builder(
                controller: _listScrollController,
                itemCount: chatList.length,
                itemBuilder: (context, index) {
                  return ChatWidget(
                    msg: chatList[index].msg,
                    chatIndex: chatList[index].chatIndex,
                  );
                },
              ),
            ),
            if (_isTyping)
              const SpinKitThreeBounce(color: Colors.white, size: 18),
            const SizedBox(height: 15),
            Material(
              color: cardColor,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  textDirection: TextDirection.rtl,
                  children: [
                    Expanded(
                      child: TextField(
                        focusNode: focusNode,
                        style: const TextStyle(color: Colors.white),
                        controller: textEditingController,
                        textAlign: TextAlign.right,
                        onSubmitted: (value) async {
                          await sendMessagesFCT();
                        },
                        decoration: const InputDecoration.collapsed(
                          hintText: "تفضل، إسألني",
                          hintStyle: TextStyle(
                              color: Color.fromARGB(255, 226, 218, 218)),
                        ),
                      ),
                    ),
                    IconButton(
                      onPressed: () async {
                        await sendMessagesFCT();
                      },
                      icon: const Icon(Icons.send, color: Colors.white),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  void scrollListToEND() {
    _listScrollController.animateTo(
      _listScrollController.position.maxScrollExtent,
      duration: const Duration(seconds: 1),
      curve: Curves.linear,
    );
  }

  Future<void> sendMessagesFCT() async {
    try {
      setState(() {
        _isTyping = true;
        chatList.add(ChatModel(msg: textEditingController.text, chatIndex: 1));
        focusNode.unfocus();
      });

      List<ChatModel> response = await ApiService.sendMessage(
        message: textEditingController.text,
      );
      setState(() => chatList.addAll(response));
    } catch (error) {
      print("Error in sendMessagesFCT: $error");
    } finally {
      textEditingController.clear();
      scrollListToEND();
      setState(() => _isTyping = false);
    }
  }
}
