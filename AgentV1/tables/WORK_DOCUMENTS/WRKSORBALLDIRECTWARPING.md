# DB2ADMIN.WRKSORBALLDIRECTWARPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 69
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204900

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `POWISEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `PRODUCTIONORDERCOUNTERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `PRODUCTIONORDERDATE` | DATE |  |  |  |  |
| 8 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 10 | `POPRDDEMANDCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `POPRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `POPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 13 | `ORIGINALWORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 16 | `WARPYARNITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `WARPYARNITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 21 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 27 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 28 | `BALLBEAMUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `BALLBEAMUGGCODE` | CHAR(3) |  |  |  |  |
| 30 | `BALLBEAMNOUSERGEGPTYCMYCODE` | CHAR(3) |  |  |  |  |
| 31 | `BALLBEAMNOCODE` | CHAR(10) |  |  |  |  |
| 32 | `RESOURCEMAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 33 | `BALLBEAMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `UOMTYPE` | CHAR(1) |  |  |  |  |
| 35 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 36 | `STARTTIME` | TIMESTAMP |  |  |  |  |
| 37 | `ENDTIME` | TIMESTAMP |  |  |  |  |
| 38 | `TOTALMINUTES` | INTEGER | NOT NULL |  |  |  |
| 39 | `NOOFENDS` | INTEGER | NOT NULL |  |  |  |
| 40 | `OPERATORUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `OPERATORUGGCODE` | CHAR(3) |  |  |  |  |
| 42 | `OPERATORUSERGEGPTYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `OPERATORCODE` | CHAR(10) |  |  |  |  |
| 44 | `MACHINESPEED` | DECIMAL(10,5) |  |  |  |  |
| 45 | `CREELTENSION` | DECIMAL(10,5) |  |  |  |  |
| 46 | `MACHINEPRESSURE` | DECIMAL(10,5) |  |  |  |  |
| 47 | `WEAKYARN` | INTEGER | NOT NULL |  |  |  |
| 48 | `HAIRINESS` | INTEGER | NOT NULL |  |  |  |
| 49 | `SNARL` | INTEGER | NOT NULL |  |  |  |
| 50 | `FAULTOFCONE` | INTEGER | NOT NULL |  |  |  |
| 51 | `BROKENEND` | INTEGER | NOT NULL |  |  |  |
| 52 | `EMPTYCONE` | INTEGER | NOT NULL |  |  |  |
| 53 | `SLUB` | INTEGER | NOT NULL |  |  |  |
| 54 | `OTHERBREAKS` | INTEGER | NOT NULL |  |  |  |
| 55 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 56 | `POSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `POSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `POSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `POSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 60 | `PDSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `PDSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 62 | `PDSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `PDSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `PDSTEPPKGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `PDSTEPPKGUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 67 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |
| 68 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORBALLDIRECTWARPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSER,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.POWISEFLAG,
       t.COMPANYCODE,
       t.PRODUCTIONORDERCOUNTERCODE,
       t.PRODUCTIONORDERCODE,
       t.PRODUCTIONORDERDATE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.POPRDDEMANDCOUNTERCOMPANYCODE,
       t.POPRODUCTIONDEMANDCOUNTERCODE
FROM   DB2ADMIN.WRKSORBALLDIRECTWARPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
