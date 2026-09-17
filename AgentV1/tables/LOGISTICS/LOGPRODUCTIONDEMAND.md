# DB2ADMIN.LOGPRODUCTIONDEMAND

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 151
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120273

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 8 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 10 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 12 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 14 | `INTERNALORDERGROUPCODE` | CHAR(15) |  |  |  |  |
| 15 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 16 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 18 | `PRORESPONSIBLECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `PRODUCTIONRESPONSIBLECODE` | CHAR(50) |  |  |  |  |
| 20 | `REFERENCEDATE` | DATE |  |  |  |  |
| 21 | `PLANNERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `PLANNERCODE` | CHAR(50) |  |  |  |  |
| 23 | `MAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 24 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 25 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 26 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 27 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 28 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 29 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 30 | `PRDDEMANDSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 31 | `ENTRYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `ENTRYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 33 | `ENTRYLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 34 | `ENTRYLOCWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 35 | `ENTRYLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 36 | `ENTRYLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 37 | `WAREHOUSEWIPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 39 | `WIPCOSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `WIPCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 41 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 43 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 44 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 49 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 50 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 51 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 52 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 53 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 54 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 55 | `ROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 56 | `SPLITTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 57 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 58 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 61 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 63 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 65 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `FINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `FINALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `FINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `FINALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `FINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `ENTEREDUSERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 74 | `ENTEREDBASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 75 | `ENTEREDUSERSECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 76 | `ENTEREDBASESECONDARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 77 | `ENTEREDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 78 | `UOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 79 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 80 | `STDPRODUCTIONBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 81 | `QUANTITYPERPERIOD` | DECIMAL(15,5) |  |  |  |  |
| 82 | `NUMBEROFPERIODS` | INTEGER | NOT NULL |  |  |  |
| 83 | `INITIALPLANNEDDATE` | DATE |  |  |  |  |
| 84 | `FINALPLANNEDDATE` | DATE |  |  |  |  |
| 85 | `INITIALPLANNEDSCHEDULEDDATE` | DATE |  |  |  |  |
| 86 | `FINALPLANNEDSCHEDULEDDATE` | DATE |  |  |  |  |
| 87 | `INITIALSCHEDULEDDATE` | DATE |  |  |  |  |
| 88 | `FINALSCHEDULEDDATE` | DATE |  |  |  |  |
| 89 | `INITIALEFFECTIVEDATE` | DATE |  |  |  |  |
| 90 | `FINALEFFECTIVEDATE` | DATE |  |  |  |  |
| 91 | `DESTINATIONORDER` | CHAR(2) | NOT NULL |  |  |  |
| 92 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 93 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 94 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 95 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 96 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 97 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 98 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 99 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 100 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 101 | `ORIGDLVSALORDLINESALORDCNTCOD` | CHAR(8) |  |  |  |  |
| 102 | `ORIGDLVSALORDLINESALORDERCODE` | CHAR(15) |  |  |  |  |
| 103 | `ORIGDLVSALORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 104 | `ORIGDLVSALORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 105 | `ORIGDLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 106 | `ORIGDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 107 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 108 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 109 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 110 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 111 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 112 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 113 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 114 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 115 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 116 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 117 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 118 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 119 | `MANUALCLOSUREREASON` | INTEGER | NOT NULL |  |  |  |
| 120 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 121 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 122 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 123 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 124 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 125 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 126 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 127 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 128 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 129 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 130 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 131 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 132 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 133 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 134 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 135 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 136 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 137 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 138 | `MAINTENANCEOFORIGDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 139 | `SUBPROJECTCODE` | DECIMAL(5,0) |  |  |  |  |
| 140 | `SPLITFROMDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 141 | `SPLITFROMDEMANDCODE` | CHAR(15) |  |  |  |  |
| 142 | `MQMSPLITREFERENCE` | CHAR(10) |  |  |  |  |
| 143 | `ORIGINALROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 144 | `PRODUCTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 145 | `SAVEDINITIALPLANNEDDATE` | DATE |  |  |  |  |
| 146 | `SAVEDFINALPLANNEDDATE` | DATE |  |  |  |  |
| 147 | `CANBEDELETEDBYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 148 | `DRCODE` | CHAR(8) |  |  |  |  |
| 149 | `DRLINE` | CHAR(15) |  |  |  |  |
| 150 | `ORIGINDRLINENR` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRODUCTIONDEMAND.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGPRODUCTIONDEMANDTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.TEMPLATECODE,
       t.TYPE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.STATISTICALGROUPCOMPANYCODE,
       t.STATISTICALGROUPCODE
FROM   DB2ADMIN.LOGPRODUCTIONDEMAND t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
