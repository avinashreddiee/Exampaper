// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataStorage {
    struct DataEntry {
        string identifier;
        string[] dataList;
    }

    DataEntry[] public dataEntries;
    mapping(string => DataEntry) private dataMap;

    // Add data in list format
    function addData(string memory _identifier, string[] memory _dataList) public {
        DataEntry memory newEntry = DataEntry({
            identifier: _identifier,
            dataList: _dataList
        });
        dataEntries.push(newEntry);
        dataMap[_identifier] = newEntry;
    }

    // Get all data for a specific identifier
    function getData(string memory _identifier) public view returns (string[] memory) {
        return dataMap[_identifier].dataList;
    }

    // Get all data entries
    function getAllData() public view returns (DataEntry[] memory) {
        return dataEntries;
    }

    // Get the total number of data entries
    function getTotalDataCount() public view returns (uint256) {
        return dataEntries.length;
    }
}
