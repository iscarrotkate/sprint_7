login_response_schema = {
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    }
  },
  "required": [
    "id"
  ]
}

place_order_response_schema = {
  "type": "object",
  "properties": {
    "track": {
      "type": "integer"
    }
  },
  "required": [
    "track"
  ]
}

orders_list_response_schema = {
  "type": "object",
  "properties": {
    "orders": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "courierId": {
            "type": ["integer", "null"]
          },
          "firstName": {
            "type": ["string", "null"]
          },
          "lastName": {
            "type": ["string", "null"]
          },
          "address": {
            "type": ["string", "null"]
          },
          "metroStation": {
            "type": ["string", "null"]
          },
          "phone": {
            "type": ["string", "null"]
          },
          "rentTime": {
            "type": ["integer", "null"]
          },
          "deliveryDate": {
            "type": ["string", "null"]
          },
          "track": {
            "type": "integer"
          },
          "color": {
            "type": ["array", "null"],
            "items": {
              "type": "string",
              "enum": ["BLACK", "GREY"]
            }
          },
          "comment": {
            "type": ["string", "null"]
          },
          "createdAt": {
            "type": "string"
          },
          "updatedAt": {
            "type": "string"
          },
          "status": {
            "type": "integer"
          }
        },
        "required": [
          "id",
          "track",
          "createdAt",
          "updatedAt",
          "status"
        ]
      }
    },
    "pageInfo": {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer"
        },
        "total": {
          "type": "integer"
        },
        "limit": {
          "type": "integer"
        }
      },
      "required": ["page", "total", "limit"]
    },
    "availableStations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "number": {
            "type": "string"
          },
          "color": {
            "type": "string"
          }
        },
        "required": ["name", "number", "color"]
      }
    }
  },
  "required": ["orders", "pageInfo", "availableStations"]
}