# DB2ADMIN.LOGPRODUCTIONDEMANDTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 90
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 207186

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `RESERVATIONMANAGED` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `RESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 13 | `EDITABLERESERVATION` | CHAR(2) |  |  |  |  |
| 14 | `ROUTINGPRODUCTIONMANAGED` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `EDITABLEROUTING` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `PRECREATEELEMENTS` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `PRECREATEELEMENTSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 18 | `COMMISSIONORDERLINK` | CHAR(2) | NOT NULL |  |  |  |
| 19 | `DATETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 20 | `PRODUCTIONORDERBLOCKED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `ALLENTITIESCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `PLANNINGBYORDERMULTILINKS` | SMALLINT | NOT NULL |  |  |  |
| 23 | `LINKEDSTOCKTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 24 | `CREATEALLOCATIONATSTOCKENTRY` | SMALLINT | NOT NULL |  |  |  |
| 25 | `KEEPORIGINDLVIFDISCONNECTED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `FINITECAPACITYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 27 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 28 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 30 | `CUSTOMERMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 31 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 32 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `COLLECTIONGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 34 | `PRDDEMANDSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `PLANNEDSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `STOCKTYPEFIRSTEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 37 | `STOCKTYPESECONDEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 38 | `STOCKTYPETHIRDEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 39 | `STOCKTYPEFOURTHEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 40 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 42 | `ENTRYSTOCKTRNTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `ENTRYSTOCKTRNTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 44 | `RETURNTRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `RETURNTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 46 | `ENTRYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `ENTRYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 48 | `ENTRYLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 49 | `ENTRYLOCWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 50 | `ENTRYLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 51 | `ENTRYLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 52 | `ENTRYALLOCATIONTYPE` | CHAR(2) |  |  |  |  |
| 53 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 55 | `LOSEDERIVATIONALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 56 | `DERIVATIONALLTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 57 | `DERIVATIONALLTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 58 | `HANDLEDYELOTUOM` | INTEGER | NOT NULL |  |  |  |
| 59 | `DYELOTUOMCODE` | CHAR(3) |  |  |  |  |
| 60 | `DYELOTSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 61 | `RECEIPTINBASEUOM` | SMALLINT | NOT NULL |  |  |  |
| 62 | `CHECKDEMANDCODE` | CHAR(20) |  |  |  |  |
| 63 | `CHECKSTEPCODE` | CHAR(20) |  |  |  |  |
| 64 | `ADSTEPVALORIZATIONCODE` | CHAR(20) |  |  |  |  |
| 65 | `STEPGROUPINGCODE` | CHAR(20) |  |  |  |  |
| 66 | `DEMANDQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 67 | `DEMANDSPLITCODE` | CHAR(20) |  |  |  |  |
| 68 | `DEMANDORDERPRINTCODE` | CHAR(20) |  |  |  |  |
| 69 | `COMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 70 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 71 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 72 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 73 | `SPLITTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 74 | `SPLITPOLICYCODE` | CHAR(20) |  |  |  |  |
| 75 | `PERIODICQTYRULECODE` | CHAR(10) |  |  |  |  |
| 76 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 77 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 78 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 79 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 80 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 81 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 82 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 83 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 84 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 85 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 86 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 87 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 88 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 89 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGPRODUCTIONDEMAND**.`ABSUNIQUEID` (high confidence — name = 'LOGPRODUCTIONDEMAND' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGPRODUCTIONDEMANDTEMPLATE.FATHERID = LOGPRODUCTIONDEMAND.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TYPE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.PROTOTYPE,
       t.RESERVATIONMANAGED
FROM   DB2ADMIN.LOGPRODUCTIONDEMANDTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
