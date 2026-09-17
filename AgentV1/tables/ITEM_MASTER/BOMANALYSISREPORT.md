# DB2ADMIN.BOMANALYSISREPORT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 86
- **Primary key**: `REPORT`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23883

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORT` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DETAILTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 15 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 16 | `FILTERTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `BOMSELLIST` | SMALLINT | NOT NULL |  |  |  |
| 18 | `SUBCODESWITHOUTCHECK` | SMALLINT | NOT NULL |  |  |  |
| 19 | `INITIALSUBCODE01` | CHAR(20) |  |  |  |  |
| 20 | `INITIALSUBCODE02` | CHAR(10) |  |  |  |  |
| 21 | `INITIALSUBCODE03` | CHAR(10) |  |  |  |  |
| 22 | `INITIALSUBCODE04` | CHAR(10) |  |  |  |  |
| 23 | `INITIALSUBCODE05` | CHAR(10) |  |  |  |  |
| 24 | `INITIALSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `INITIALSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `INITIALSUBCODE08` | CHAR(10) |  |  |  |  |
| 27 | `INITIALSUBCODE09` | CHAR(10) |  |  |  |  |
| 28 | `INITIALSUBCODE10` | CHAR(10) |  |  |  |  |
| 29 | `FINALSUBCODE01` | CHAR(20) |  |  |  |  |
| 30 | `FINALSUBCODE02` | CHAR(10) |  |  |  |  |
| 31 | `FINALSUBCODE03` | CHAR(10) |  |  |  |  |
| 32 | `FINALSUBCODE04` | CHAR(10) |  |  |  |  |
| 33 | `FINALSUBCODE05` | CHAR(10) |  |  |  |  |
| 34 | `FINALSUBCODE06` | CHAR(10) |  |  |  |  |
| 35 | `FINALSUBCODE07` | CHAR(10) |  |  |  |  |
| 36 | `FINALSUBCODE08` | CHAR(10) |  |  |  |  |
| 37 | `FINALSUBCODE09` | CHAR(10) |  |  |  |  |
| 38 | `FINALSUBCODE10` | CHAR(10) |  |  |  |  |
| 39 | `USERQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `USERQTY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `ASSEMBLYQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `ASSEMBLYQTY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `AVAILABILITYQUANTITYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 45 | `AVAILABILITYFORMULACODE` | CHAR(3) |  |  |  |  |
| 46 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 47 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 48 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 49 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 50 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 51 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 52 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 53 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 54 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 55 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 56 | `BOMCODE` | VARCHAR(120) |  |  |  |  |
| 57 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 58 | `BOMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 59 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 60 | `INCLUDEALLGENREF` | SMALLINT | NOT NULL |  |  |  |
| 61 | `CHECKCODE` | CHAR(2) |  |  |  |  |
| 62 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 63 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 64 | `INCLUDEALLPLANT` | SMALLINT | NOT NULL |  |  |  |
| 65 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 66 | `INCLUDEALLCOSTGROUP` | SMALLINT | NOT NULL |  |  |  |
| 67 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 68 | `INCLUDETECHNICALBOM` | SMALLINT | NOT NULL |  |  |  |
| 69 | `INCLUDEPRODUCTIONBOM` | SMALLINT | NOT NULL |  |  |  |
| 70 | `INCLUDECOSTCALCULATIONBOM` | SMALLINT | NOT NULL |  |  |  |
| 71 | `USESSELECTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 72 | `SUSPENDEDBOM` | SMALLINT | NOT NULL |  |  |  |
| 73 | `APPROVEDBOM` | SMALLINT | NOT NULL |  |  |  |
| 74 | `ACTIVEBOM` | SMALLINT | NOT NULL |  |  |  |
| 75 | `BESTINCIDENCE` | SMALLINT | NOT NULL |  |  |  |
| 76 | `VALIDITYDATE` | DATE |  |  |  |  |
| 77 | `ENGCHGSELNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 78 | `PRODUCTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 79 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 80 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 81 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 82 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `AVAILABILITYFORMULACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `USERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMANALYSISREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.REPORT,
       t.COMPANYCODE,
       t.DETAILTYPE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.BOMANALYSISREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
