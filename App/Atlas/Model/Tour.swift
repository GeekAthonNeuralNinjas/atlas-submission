//
//  Trip.swift
//  Atlas
//
//  Created by Miguel Susano on 23/11/2024.
//  Copyright © 2024 com.miguel. All rights reserved.
//
import Foundation
import SwiftData
import MapKit

@Model
final class Tour: Identifiable {
    var id: String
    var name: String
    var text: String
    @Relationship(deleteRule: .cascade) var places: [Place]
    var isFavorite: Bool = false
    
    init(id: String = UUID().uuidString, name: String, places: [Place] = [], text: String) {
        self.id = id
        self.name = name
        self.text = text
        self.places = places
    }
}
