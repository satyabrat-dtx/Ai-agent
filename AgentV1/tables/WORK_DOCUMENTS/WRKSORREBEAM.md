# DB2ADMIN.WRKSORREBEAM

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 59
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204999

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
| 16 | `PREVIOUSBALLBEAMNO` | CHAR(10) |  |  |  |  |
| 17 | `PREVIOUSROPEDYEMACHINE` | CHAR(50) |  |  |  |  |
| 18 | `PREVIOUSBALLMTR` | DECIMAL(15,5) |  |  |  |  |
| 19 | `PREVIOUSNOOFENDS` | INTEGER | NOT NULL |  |  |  |
| 20 | `PREVIOUSDRUMNO` | CHAR(10) |  |  |  |  |
| 21 | `PREVIOUSROPEPOSITIONNO` | INTEGER | NOT NULL |  |  |  |
| 22 | `PREVIOUSROPEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `STARTTIME` | TIMESTAMP |  |  |  |  |
| 24 | `ENDTIME` | TIMESTAMP |  |  |  |  |
| 25 | `TOTALMINUTES` | INTEGER | NOT NULL |  |  |  |
| 26 | `RESOURCEMAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 27 | `UOMTYPE` | CHAR(1) |  |  |  |  |
| 28 | `BEAMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 30 | `REBEAMNOUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `REBEAMNOUGGCODE` | CHAR(3) |  |  |  |  |
| 32 | `REBEAMNOUSERGEGPTYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `REBEAMNOCODE` | CHAR(10) |  |  |  |  |
| 34 | `OPERATORUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `OPERATORUGGCODE` | CHAR(3) |  |  |  |  |
| 36 | `OPERATORUSERGEGPTYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `OPERATORCODE` | CHAR(10) |  |  |  |  |
| 38 | `LOOSINGENDS` | INTEGER | NOT NULL |  |  |  |
| 39 | `FLUFF` | INTEGER | NOT NULL |  |  |  |
| 40 | `HAIRINESS` | INTEGER | NOT NULL |  |  |  |
| 41 | `STICKYEND` | INTEGER | NOT NULL |  |  |  |
| 42 | `WETYARN` | INTEGER | NOT NULL |  |  |  |
| 43 | `SHORTENDS` | INTEGER | NOT NULL |  |  |  |
| 44 | `OTHERBREAKS` | INTEGER | NOT NULL |  |  |  |
| 45 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 46 | `POSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `POSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `POSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `POSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `PDSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `PDSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `PDSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `PDSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 54 | `PDSTEPPKGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `PDSTEPPKGUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 57 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |
| 58 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORREBEAMUID` (ABSUNIQUEID)

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
FROM   DB2ADMIN.WRKSORREBEAM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
