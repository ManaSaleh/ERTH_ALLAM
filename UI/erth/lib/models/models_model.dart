class ModelsModel {
  final String id;
  final int created;
  final String root;

  ModelsModel({required this.id, required this.created, required this.root});

  factory ModelsModel.fromJson(Map<String, dynamic> json) {
    return ModelsModel(
      id: json["id"] ?? "Unknown ID",      // Provide default value if id is null
      created: json["created"] ?? 0,        // Default to 0 if created is null
      root: json["root"] ?? "Unknown Root", // Default value if root is null
    );
  }

  static List<ModelsModel> modelFromSnapshot(List modelSnapshot) {
    return modelSnapshot.map((data) => ModelsModel.fromJson(data)).toList();
  }
}
