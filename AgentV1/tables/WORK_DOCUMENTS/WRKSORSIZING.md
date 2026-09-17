# DB2ADMIN.WRKSORSIZING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205652

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
| 16 | `RESOURCEMAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 17 | `STARTTIME` | TIMESTAMP |  |  |  |  |
| 18 | `ENDTIME` | TIMESTAMP |  |  |  |  |
| 19 | `TOTALMINUTES` | INTEGER | NOT NULL |  |  |  |
| 20 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 23 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 25 | `SIZEBEAMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `UOMTYPE` | CHAR(1) |  |  |  |  |
| 27 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 28 | `OPERATORUGGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `OPERATORUGGCODE` | CHAR(3) |  |  |  |  |
| 30 | `OPERATORUSERGEGPTYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `OPERATORCODE` | CHAR(10) |  |  |  |  |
| 32 | `HEADBREAK` | INTEGER | NOT NULL |  |  |  |
| 33 | `CREELBREAK` | INTEGER | NOT NULL |  |  |  |
| 34 | `SHORTENDS` | INTEGER | NOT NULL |  |  |  |
| 35 | `FLUFF` | INTEGER | NOT NULL |  |  |  |
| 36 | `CROSSINGEND` | INTEGER | NOT NULL |  |  |  |
| 37 | `RBTBREAK` | INTEGER | NOT NULL |  |  |  |
| 38 | `OTHERBREAKS` | INTEGER | NOT NULL |  |  |  |
| 39 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 40 | `POSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `POSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `POSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `POSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `PDSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `PDSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `PDSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `PDSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `PDSTEPPKGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `PDSTEPPKGUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 51 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |
| 52 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORSIZINGUID` (ABSUNIQUEID)

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
FROM   DB2ADMIN.WRKSORSIZING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
