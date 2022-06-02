namespace PG {
	public class CameraCreateCommand
	{
		public const string CommandNameLabel = "CameraCreate";
		public const string NewIdLabel = "NewId";
	}

	public class CameraFitCommand
	{
		public const string CameraFitCommandLabel = "CameraFit";
		public const string CameraXYCommandLabel = "CameraXY";
		public const string CameraYZCommandLabel = "CameraYZ";
		public const string CameraZXCommandLabel = "CameraZX";
	}

	public class CameraGetCommand
	{
		public const string CommandNameLabel = "CameraGet";
		public const string NearLabel = "Near";
		public const string FarLabel = "Far";
		public const string EyePositionLabel = "EyePosition";
		public const string TargetPositionLabel = "TargetPosition";
		public const string UpVectorLabel = "UpVector";
		public const string ProjectionMatrixLabel = "ProjectionMatrix";
		public const string RotationMatrixLabel = "RotationMatrix";
	}

	public class CameraRotateCommand
	{
		public const string CameraRotateCommandLabel = "CameraRotate";
		public const string MatrixLabel = "Matrix";
	}

	public class CameraSetCommand
	{
		public const string CommandLabel = "CameraSet";
		public const string NearLabel = "Near";
		public const string FarLabel = "Far";
		public const string EyePositionLabel = "EyePosition";
		public const string TargetPositionLabel = "TargetPosition";
		public const string UpVector = "UpVector";
	}

	public class CameraTranslateCommand
	{
		public const string TranslateLabel = "Translate";
		public const string CameraTranslateCommandLabel = "CameraTranslate";
	}

	public class CameraZoomCommand
	{
		public const string CameraZoomCommandLabel = "CameraZoom";
		public const string ZoomRatioLabel = "Ratio";
	}

	public class ClearCommand
	{
		public const string CommandNameLabel = "ClearCommand";
	}

	public class Command
	{
	}

	public class CommandFactory
	{
	}

	public class DeleteCommand
	{
		public const string CommandNameLabel = "DeleteCommand";
		public const string IdLabel = "Id";
	}

	public class FileExportCommand
	{
		public const string FileExportCommandLabel = "FileExport";
		public const string FilePathLabel = "FilePath";
	}

	public class FileImportCommand
	{
		public const string FileImportCommandLabel = "FileImport";
		public const string FilePathLabel = "FilePath";
		public const string IsOkLabel = "IsOk";
		public const string NewIdLabel = "NewId";
		public const string STLFileImportCommandLabel = "STLFileImport";
	}

	public class GetCommand
	{
		public const string PositionLabel = "Position";
		public const string SceneCountLabel = "SceneCount";
		public const string SceneListIdsLabel = "SceneListIds";
		public const string MaterialNameLabel = "MaterialName";
	}

	public class ICommand
	{
	}

	public class JSONConverter
	{
	}

	public class JSONFileReader
	{
	}

	public class JSONFileWriter
	{
	}

	public class LightCreateCommand
	{
		public const string CommandNameLabel = "LightCreate";
		public const string PositionLabel = "Position";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class LightGetCommand
	{
		public const string CommandNameLabel = "LightGet";
		public const string IdLabel = "Id";
		public const string PositionLabel = "Position";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string NameLabel = "Name";
	}

	public class LightSetCommand
	{
		public const string CommandNameLabel = "LightSet";
		public const string IdLabel = "Id";
		public const string PositionLabel = "Position";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string NameLabel = "Name";
	}

	public class MaterialCreateCommand
	{
		public const string CommandNameLabel = "MaterialCreate";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string ShininessLabel = "Shininess";
		public const string AmbientTextureNameLabel = "AmbientTextureName";
		public const string DiffuseTextureNameLabel = "DiffuseTextureName";
		public const string SpecularTextureNameLabel = "SpecularTextureName";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class MaterialGetCommand
	{
		public const string CommandNameLabel = "MaterialGet";
		public const string IdLabel = "Id";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string ShininessLabel = "Shininess";
		public const string TextureNameLabel = "TextureName";
		public const string NameLabel = "Name";
	}

	public class MaterialSetCommand
	{
		public const string CommandNameLabel = "MaterialSet";
		public const string IdLabel = "Id";
		public const string AmbientLabel = "Ambient";
		public const string DiffuseLabel = "Diffuse";
		public const string SpecularLabel = "Specular";
		public const string ShininessLabel = "Shininess";
		public const string TextureNameLabel = "TextureName";
		public const string NameLabel = "Name";
	}

	public class MockCommand
	{
		public const string MockCommandLabel = "Mock";
	}

	public class NewCommand
	{
		public const string CommandNameLabel = "NewCommand";
	}

	public class OBJFileExportCommand
	{
		public const string CommandNameLabel = "OBJFileExport";
		public const string FilePathLabel = "FilePath";
		public const string IdsLabel = "Ids";
	}

	public class OBJFileImportCommand
	{
		public const string CommandNameLabel = "OBJFileImport";
		public const string FilePathLabel = "FilePath";
		public const string NewIdLabel = "NewId";
	}

	public class ParticleSystemCreateCommand
	{
		public const string ParticleSystemAddLabel = "ParticleSystemAdd";
		public const string PositionsLabel = "Positions";
		public const string PointSizeLabel = "PointSize";
		public const string ColorLabel = "Color";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class ParticleSystemGetCommand
	{
		public const string CommandNameLabel = "ParticleSystemGet";
		public const string PSIdLabel = "PSId";
		public const string LayerLabel = "Layer";
		public const string PositionsLabel = "Positions";
		public const string PointSizeLabel = "PointSize";
		public const string ColorLabel = "Color";
		public const string NameLabel = "Name";
	}

	public class ParticleSystemSetCommand
	{
		public const string CommandNameLabel = "ParticleSystemSet";
		public const string IdLabel = "Id";
		public const string PositionsLabel = "Positions";
		public const string PointSizeLabel = "PointSize";
		public const string ColorLabel = "Color";
		public const string NameLabel = "Name";
		public const string LayerLabel = "Layer";
		public const string NewIdLabel = "NewId";
	}

	public class PCDFileExportCommand
	{
		public const string CommandNameLabel = "PCDFileExport";
		public const string FilePathLabel = "FilePath";
		public const string IdsLabel = "Ids";
		public const string IsBinaryLabel = "IsBinary";
	}

	public class PCDFileImportCommand
	{
		public const string CommandNameLabel = "PCDFileImport";
		public const string FilePathLabel = "FilePath";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
	}

	public class PickCommand
	{
		public const string PickCommandLabel = "Pick";
		public const string PositionLabel = "Position";
		public const string ParentIdLabel = "ParentId";
		public const string ChildIdLabel = "ChildId";
	}

	public class PLYFileExportCommand
	{
		public const string CommandNameLabel = "PLYFileExport";
		public const string FilePathLabel = "FilePath";
		public const string IdsLabel = "Ids";
		public const string IsBinaryLabel = "IsBinary";
	}

	public class PLYFileImportCommand
	{
		public const string CommandNameLabel = "PLYFileImport";
		public const string FilePathLabel = "FilePath";
		public const string ParticleSystemIdLabel = "ParticleSystemId";
	}

	public class PolygonMeshAddFacesCommand
	{
		public const string CommandNameLabel = "PolygonMeshAddFaces";
		public const string PolygonMeshIdLabel = "PolygonMeshId";
		public const string VertexIdsLabel = "VertexIds";
	}

	public class PolygonMeshAddVerticesCommand
	{
		public const string CommandNameLabel = "PolygonMeshAddVertices";
		public const string PolygonMeshIdLabel = "PolygonMeshId";
		public const string PositionIdsLabel = "PositionIds";
		public const string NormalIdsLabel = "NormalIds";
		public const string TexCoordIdsLabel = "TexCoordIds";
	}

	public class PolygonMeshCreateCommand
	{
		public const string CommandNameLabel = "PolygonMeshCreate";
		public const string PositionsLabel = "Positions";
		public const string NormalsLabel = "Normals";
		public const string TexCoordsLabel = "TexCoords";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class PresenterSetCommand
	{
		public const string CommandNameLabel = "PresenterSet";
		public const string IdLabel = "Id";
		public const string PresenterNameLabel = "PresenterName";
	}

	public class SceneGetCommand
	{
		public const string CommandLabel = "SceneGet";
		public const string IdLabel = "Id";
		public const string BoundingBoxLabel = "BoundingBox";
		public const string IsPickableLabel = "IsPickable";
		public const string IsVisibleLabel = "IsVisible";
		public const string NameLabel = "Name";
		public const string TypeNameLabel = "TypeName";
	}

	public class SceneSetCommand
	{
		public const string CommandNameLabel = "SceneSet";
		public const string IdLabel = "Id";
		public const string NameLabel = "Name";
	}

	public class ShaderBuildCommand
	{
		public const string CommandNameLabel = "ShaderBuild";
		public const string IdLabel = "Id";
	}

	public class ShaderSendCommand
	{
		public const string CommandNameLabel = "ShaderSend";
		public const string IdLabel = "Id";
	}

	public class ShapeSelectCommand
	{
		public const string CommandNameLabel = "ShapeSelectCommand";
		public const string ShapeIdLabel = "ShapeId";
	}

	public class SolidCreateCommand
	{
		public const string ParticleSystemAddLabel = "SolidCreate";
		public const string BoxLabel = "Box";
		public const string ColorLabel = "Color";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class STLFileExportCommand
	{
		public const string CommandNameLabel = "STLFileExport";
		public const string FilePathLabel = "FilePath";
		public const string IdsLabel = "Ids";
		public const string IsBinaryLabel = "IsBinary";
	}

	public class STLFileImportCommand
	{
		public const string CommandNameLabel = "STLFileImport";
		public const string FilePathLabel = "FilePath";
		public const string TriangleMeshIdLabel = "TriangleMeshId";
	}

	public class TextureCreateCommand
	{
		public const string CommandNameLabel = "TextureCreate";
		public const string FilePathLabel = "FilePath";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class TextureSetCommand
	{
		public const string CommandNameLabel = "TextureSet";
		public const string IdLabel = "Id";
		public const string FilePathLabel = "FilePath";
		public const string IsOkLabel = "IsOk";
	}

	public class TransformCommand
	{
		public const string TransformCommandLabel = "Transform";
		public const string IdLabel = "Id";
		public const string MatrixLabel = "Matrix";
	}

	public class TriangleMeshCreateCommand
	{
		public const string CommandNameLabel = "TriangleMeshCreate";
		public const string TrianglesLabel = "Triangles";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

	public class TriangleMeshGetCommand
	{
		public const string CommandNameLabel = "TriangleMeshGet";
		public const string MeshIdLabel = "MeshId";
		public const string LayerLabel = "Layer";
		public const string TrianglesLabel = "Triangles";
		public const string NormalsLabel = "Normals";
		public const string NameLabel = "Name";
	}

	public class TriangleMeshSetCommand
	{
		public const string CommandNameLabel = "TriangleMeshSet";
		public const string MeshIdLabel = "MeshId";
		public const string TrianglesLabel = "Triangles";
	}

	public class TrimCommand
	{
		public const string TrimCommandLabel = "Trim";
		public const string ShapeIdLabel = "ShapeId";
		public const string SpaceLabel = "Space";
		public const string NewIdLabel = "NewId";
	}

	public class TXTFileExportCommand
	{
		public const string CommandNameLabel = "TXTFileExport";
		public const string FilePathLabel = "FilePath";
		public const string IdsLabel = "Ids";
	}

	public class TXTFileImportCommand
	{
		public const string CommandNameLabel = "TXTFileImport";
		public const string FilePathLabel = "FilePath";
		public const string IdLabel = "Id";
	}

	public class WireFrameCreateCommand
	{
		public const string WireFrameCreateLabel = "WireFrameCreate";
		public const string PositionsLabel = "Positions";
		public const string EdgeIndicesLabel = "EdgeIndices";
		public const string LineWidthLabel = "LineWidth";
		public const string ColorLabel = "Color";
		public const string NameLabel = "Name";
		public const string NewIdLabel = "NewId";
	}

}
