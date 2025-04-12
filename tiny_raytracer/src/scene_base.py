class SceneBase:
    """
    Scene base class. Classes derived from this should be either scenes or scene objects.
    """

    def __str__(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )

    def to_json(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )
