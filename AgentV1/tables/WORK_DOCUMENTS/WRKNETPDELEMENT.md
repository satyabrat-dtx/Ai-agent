# DB2ADMIN.WRKNETPDELEMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131161

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `FORCE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LINETOEXPLODE` | INTEGER | NOT NULL |  |  |  |
| 6 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `PCSPERBUNDLE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 22 | `NOOFBUNDLE` | INTEGER | NOT NULL |  |  |  |
| 23 | `WEFTLOT` | INTEGER | NOT NULL |  |  |  |
| 24 | `MACHINECODE` | CHAR(8) |  |  |  |  |
| 25 | `DEMANDQTY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 26 | `TOTALQTY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 27 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSER,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.FORCE,
       t.LINETOEXPLODE,
       t.PRODUCTIONORDERCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01
FROM   DB2ADMIN.WRKNETPDELEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
