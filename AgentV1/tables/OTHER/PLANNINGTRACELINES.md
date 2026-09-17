# DB2ADMIN.PLANNINGTRACELINES

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 113
- **Primary key**: `PLANNINGTRACECOMPANYCODE`, `PLANNINGTRACECREATIONID`, `PLANNINGTRACELINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 71148

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANNINGTRACECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `PLANNINGTRACECREATIONID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PLANNINGTRACELINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RECORDTYPE` | CHAR(1) |  |  |  |  |
| 5 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 6 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `FULLITEMITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `FULLITEMSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `FULLITEMSUBCODE02` | CHAR(10) |  |  |  |  |
| 14 | `FULLITEMSUBCODE03` | CHAR(10) |  |  |  |  |
| 15 | `FULLITEMSUBCODE04` | CHAR(10) |  |  |  |  |
| 16 | `FULLITEMSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `FULLITEMSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `FULLITEMSUBCODE07` | CHAR(10) |  |  |  |  |
| 19 | `FULLITEMSUBCODE08` | CHAR(10) |  |  |  |  |
| 20 | `FULLITEMSUBCODE09` | CHAR(10) |  |  |  |  |
| 21 | `FULLITEMSUBCODE10` | CHAR(10) |  |  |  |  |
| 22 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 23 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 24 | `PERIODTYPECODE` | CHAR(10) |  |  |  |  |
| 25 | `PERIODYEAR` | DECIMAL(4,0) |  |  |  |  |
| 26 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 27 | `PERIODSPLITNR` | INTEGER | NOT NULL |  |  |  |
| 28 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 29 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 30 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 32 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 33 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 34 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 35 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 36 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 37 | `REQUISITIONREQUISITIONTMPCODE` | CHAR(3) |  |  |  |  |
| 38 | `REQUISITIONCODE` | CHAR(15) |  |  |  |  |
| 39 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 43 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 45 | `NETTEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `NETTEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `NETTEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `FORECASTUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `FORECASTUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `FORECASTUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `ALLOCATION1` | CHAR(15) |  |  |  |  |
| 52 | `ALLOCATION2` | CHAR(15) |  |  |  |  |
| 53 | `ALLOCATION3` | CHAR(15) |  |  |  |  |
| 54 | `ALLOCATION4` | CHAR(15) |  |  |  |  |
| 55 | `ALLOCATION5` | CHAR(15) |  |  |  |  |
| 56 | `NETTINGINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 57 | `NETTINGINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 58 | `WARNINGDETAIL` | CHAR(1) |  |  |  |  |
| 59 | `NETTINGINTORDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 60 | `NETTINGINTORDCODE` | CHAR(15) |  |  |  |  |
| 61 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 62 | `EXPLOSIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 63 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 65 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 68 | `SHIFTDATE` | SMALLINT | NOT NULL |  |  |  |
| 69 | `FORCEDDATE` | SMALLINT | NOT NULL |  |  |  |
| 70 | `CONFIRMED` | SMALLINT | NOT NULL |  |  |  |
| 71 | `DELETED` | SMALLINT | NOT NULL |  |  |  |
| 72 | `EXPLOSIONLEVEL` | INTEGER | NOT NULL |  |  |  |
| 73 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 75 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 76 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 77 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 78 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 79 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 80 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 81 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 82 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 83 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 84 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `EXPLOSIONWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 89 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 90 | `REQHEADERCODE` | CHAR(15) |  |  |  |  |
| 91 | `REQHEADERLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 92 | `ALLOCATION6` | CHAR(15) |  |  |  |  |
| 93 | `ALLOCATION7` | CHAR(15) |  |  |  |  |
| 94 | `ALLOCATION8` | CHAR(15) |  |  |  |  |
| 95 | `ALLOCATION9` | CHAR(15) |  |  |  |  |
| 96 | `ALLOCATION10` | CHAR(15) |  |  |  |  |
| 97 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 98 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 99 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 100 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 101 | `DELIVERYDATE` | DATE |  |  |  |  |
| 102 | `PLANNEDDATE` | DATE |  |  |  |  |
| 103 | `PURCHASEDATE` | DATE |  |  |  |  |
| 104 | `PRODRESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 105 | `PRODRESORDERCODE` | CHAR(15) |  |  |  |  |
| 106 | `PRODRESRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 107 | `PURDLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 108 | `PURDLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 109 | `PURDLVPURORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 110 | `PURDLVPURORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 111 | `PURDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 112 | `LINKEDSTOCKNUMBERID` | DECIMAL(11,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PLANNINGTRACECOMPANYCODE,
       t.PLANNINGTRACECREATIONID,
       t.PLANNINGTRACELINE,
       t.SUBLINE,
       t.RECORDTYPE,
       t.DLVSALORDLINESALORDCNTCODE,
       t.DLVSALORDERLINESALESORDERCODE,
       t.DLVSALESORDERLINEORDERLINE,
       t.DLVSALESORDERLINEORDERSUBLINE,
       t.DLVSALORDLINECMPORDERLINE,
       t.DELIVERYDELIVERYLINE,
       t.FULLITEMITEMTYPECODE
FROM   DB2ADMIN.PLANNINGTRACELINES t
FETCH FIRST 100 ROWS ONLY;
```
