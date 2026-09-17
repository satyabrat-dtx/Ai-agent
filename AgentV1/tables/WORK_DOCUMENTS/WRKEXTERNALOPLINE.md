# DB2ADMIN.WRKEXTERNALOPLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 65
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30643

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 3 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `EXTERNOPLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `EXTERNOPLINECODE` | CHAR(15) |  |  |  |  |
| 8 | `EXTERNOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 9 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `STEPPRODEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `STEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 12 | `STEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 13 | `PRDRESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `PRDRESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 15 | `PRDRESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 17 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 18 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 19 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 20 | `ELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 22 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 23 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 34 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SERVICEITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 44 | `SERVICESUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 45 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 46 | `ENTRYITEMCODE` | VARCHAR(120) |  |  |  |  |
| 47 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 48 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 49 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 50 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 51 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 52 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 53 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `ELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 55 | `SERVICEITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 56 | `ENTRYITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 57 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 59 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 60 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 62 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 63 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 64 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LINETEMPLATECODE,
       t.DIVISIONCODE,
       t.ORDERTYPE,
       t.EXTERNOPLINECOUNTERCODE,
       t.EXTERNOPLINECODE,
       t.EXTERNOPLINEORDERLINE,
       t.ORIGINTYPE,
       t.STEPPRODEMANDCOUNTERCODE,
       t.STEPPRODUCTIONDEMANDCODE
FROM   DB2ADMIN.WRKEXTERNALOPLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
