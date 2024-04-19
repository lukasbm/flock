class Experiment:

    @property
    def tags(self) -> List[str]:
        return self._tags

    @property
    def run_id(self) -> str:
        return self._run_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    def upload(self):
        pass

    def rerun(self):
        pass
