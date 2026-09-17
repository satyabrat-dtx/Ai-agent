# DB2ADMIN.WRKSORROPEDYEING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `POWISEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ROPEPOSITIONNO` | INTEGER | NOT NULL |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `PRODUCTIONORDERCOUNTERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 7 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 8 | `PRODUCTIONORDERDATE` | DATE |  |  |  |  |
| 9 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 11 | `POPRDDEMANDCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `POPRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `POPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 14 | `ORIGINALWORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 16 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 17 | `PREVIOUSBALLBEAMNO` | CHAR(10) |  |  |  |  |
| 18 | `PREVIOUSBWMACHINE` | CHAR(50) |  |  |  |  |
| 19 | `PREVIOUSBALLMTR` | DECIMAL(15,5) |  |  |  |  |
| 20 | `PREVIOUSNOOFENDS` | INTEGER | NOT NULL |  |  |  |
| 21 | `RESOURCEMAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 22 | `DRUMNOUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `DRUMNOUGGCODE` | CHAR(3) |  |  |  |  |
| 24 | `DRUMNOUSERGEGPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `DRUMNOCODE` | CHAR(10) |  |  |  |  |
| 26 | `ROPEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `UOMTYPE` | CHAR(1) |  |  |  |  |
| 28 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 29 | `STARTTIME` | TIMESTAMP |  |  |  |  |
| 30 | `ENDTIME` | TIMESTAMP |  |  |  |  |
| 31 | `TOTALMINUTES` | INTEGER | NOT NULL |  |  |  |
| 32 | `OPERATORUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `OPERATORUGGCODE` | CHAR(3) |  |  |  |  |
| 34 | `OPERATORUSERGEGPTYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `OPERATORCODE` | CHAR(10) |  |  |  |  |
| 36 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 37 | `POSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `POSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `POSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `POSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `PDSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `PDSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 43 | `PDSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `PDSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 45 | `PDSTEPPKGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `PDSTEPPKGUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 48 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORROPEDYEINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSER,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.POWISEFLAG,
       t.ROPEPOSITIONNO,
       t.COMPANYCODE,
       t.PRODUCTIONORDERCOUNTERCODE,
       t.PRODUCTIONORDERCODE,
       t.PRODUCTIONORDERDATE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.POPRDDEMANDCOUNTERCOMPANYCODE
FROM   DB2ADMIN.WRKSORROPEDYEING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
