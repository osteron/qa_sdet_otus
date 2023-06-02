from pydantic import BaseModel
from typing import List, Optional


class Message(BaseModel):
    african: List[Optional[str]]
    affenpinscher: List[Optional[str]]
    african: List[Optional[str]]
    airedale: List[Optional[str]]
    akita: List[Optional[str]]
    appenzeller: List[Optional[str]]
    australian: List[Optional[str]]
    basenji: List[Optional[str]]
    beagle: List[Optional[str]]
    bluetick: List[Optional[str]]
    borzoi: List[Optional[str]]
    bouvier: List[Optional[str]]
    boxer: List[Optional[str]]
    brabancon: List[Optional[str]]
    briard: List[Optional[str]]
    buhund: List[Optional[str]]
    bulldog: List[Optional[str]]
    bullterrier: List[Optional[str]]
    cattledog: List[Optional[str]]
    chihuahua: List[Optional[str]]
    chow: List[Optional[str]]
    clumber: List[Optional[str]]
    cockapoo: List[Optional[str]]
    collie: List[Optional[str]]
    coonhound: List[Optional[str]]
    corgi: List[Optional[str]]
    cotondetulear: List[Optional[str]]
    dachshund: List[Optional[str]]
    dalmatian: List[Optional[str]]
    dane: List[Optional[str]]
    deerhound: List[Optional[str]]
    dhole: List[Optional[str]]
    dingo: List[Optional[str]]
    doberman: List[Optional[str]]
    elkhound: List[Optional[str]]
    entlebucher: List[Optional[str]]
    eskimo: List[Optional[str]]
    finnish: List[Optional[str]]
    frise: List[Optional[str]]
    germanshepherd: List[Optional[str]]
    greyhound: List[Optional[str]]
    groenendael: List[Optional[str]]
    havanese: List[Optional[str]]
    hound: List[Optional[str]]
    husky: List[Optional[str]]
    keeshond: List[Optional[str]]
    kelpie: List[Optional[str]]
    komondor: List[Optional[str]]
    kuvasz: List[Optional[str]]
    labradoodle: List[Optional[str]]
    labrador: List[Optional[str]]
    leonberg: List[Optional[str]]
    lhasa: List[Optional[str]]
    malamute: List[Optional[str]]
    malinois: List[Optional[str]]
    maltese: List[Optional[str]]
    mastiff: List[Optional[str]]
    mexicanhairless: List[Optional[str]]
    mix: List[Optional[str]]
    mountain: List[Optional[str]]
    newfoundland: List[Optional[str]]
    otterhound: List[Optional[str]]
    ovcharka: List[Optional[str]]
    papillon: List[Optional[str]]
    pekinese: List[Optional[str]]
    pembroke: List[Optional[str]]
    pinscher: List[Optional[str]]
    pitbull: List[Optional[str]]
    pointer: List[Optional[str]]
    pomeranian: List[Optional[str]]
    poodle: List[Optional[str]]
    pug: List[Optional[str]]
    puggle: List[Optional[str]]
    pyrenees: List[Optional[str]]
    redbone: List[Optional[str]]
    retriever: List[Optional[str]]
    ridgeback: List[Optional[str]]
    rottweiler: List[Optional[str]]
    saluki: List[Optional[str]]
    samoyed: List[Optional[str]]
    schipperke: List[Optional[str]]
    schnauzer: List[Optional[str]]
    segugio: List[Optional[str]]
    setter: List[Optional[str]]
    sharpei: List[Optional[str]]
    sheepdog: List[Optional[str]]
    shiba: List[Optional[str]]
    shihtzu: List[Optional[str]]
    spaniel: List[Optional[str]]
    spitz: List[Optional[str]]
    springer: List[Optional[str]]
    stbernard: List[Optional[str]]
    terrier: List[Optional[str]]
    tervuren: List[Optional[str]]
    vizsla: List[Optional[str]]
    waterdog: List[Optional[str]]
    weimaraner: List[Optional[str]]
    whippet: List[Optional[str]]
    wolfhound: List[Optional[str]]


class GetResponseDogModel(BaseModel):
    message: str
    status: str


class GetResponseListDogModel(BaseModel):
    message: list[str]
    status: str


class GetResponseListBreedsModel(BaseModel):
    message: Message
    status: str
