class ChatModel {
  final String msg;
  final int chatIndex;

  ChatModel({required this.msg, required this.chatIndex});

  factory ChatModel.fromJson(Map<String, dynamic> json) => ChatModel(
      msg: json["msg"] ?? "null msg", // Provide default value if msg is null
      chatIndex: json["chatIndex"] ?? 0);
}
