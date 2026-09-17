# DB2ADMIN.WRKSTOPPAGELOSS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131920

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 6 | `WRKCENTER` | CHAR(15) |  |  |  |  |
| 7 | `RESOURCENO` | CHAR(8) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `CODECODE` | CHAR(10) |  |  |  |  |
| 10 | `DESCCODE` | CHAR(100) |  |  |  |  |
| 11 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 12 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 13 | `SHIFT` | INTEGER | NOT NULL |  |  |  |
| 14 | `D1` | DECIMAL(18,5) |  |  |  |  |
| 15 | `D2` | DECIMAL(18,5) |  |  |  |  |
| 16 | `D3` | DECIMAL(18,5) |  |  |  |  |
| 17 | `D4` | DECIMAL(18,5) |  |  |  |  |
| 18 | `D5` | DECIMAL(18,5) |  |  |  |  |
| 19 | `D6` | DECIMAL(18,5) |  |  |  |  |
| 20 | `D7` | DECIMAL(18,5) |  |  |  |  |
| 21 | `D8` | DECIMAL(18,5) |  |  |  |  |
| 22 | `D9` | DECIMAL(18,5) |  |  |  |  |
| 23 | `D10` | DECIMAL(18,5) |  |  |  |  |
| 24 | `D11` | DECIMAL(18,5) |  |  |  |  |
| 25 | `D12` | DECIMAL(18,5) |  |  |  |  |
| 26 | `D13` | DECIMAL(18,5) |  |  |  |  |
| 27 | `D14` | DECIMAL(18,5) |  |  |  |  |
| 28 | `D15` | DECIMAL(18,5) |  |  |  |  |
| 29 | `D16` | DECIMAL(18,5) |  |  |  |  |
| 30 | `D17` | DECIMAL(18,5) |  |  |  |  |
| 31 | `D18` | DECIMAL(18,5) |  |  |  |  |
| 32 | `D19` | DECIMAL(18,5) |  |  |  |  |
| 33 | `D20` | DECIMAL(18,5) |  |  |  |  |
| 34 | `D21` | DECIMAL(18,5) |  |  |  |  |
| 35 | `D22` | DECIMAL(18,5) |  |  |  |  |
| 36 | `D23` | DECIMAL(18,5) |  |  |  |  |
| 37 | `D24` | DECIMAL(18,5) |  |  |  |  |
| 38 | `D25` | DECIMAL(18,5) |  |  |  |  |
| 39 | `D26` | DECIMAL(18,5) |  |  |  |  |
| 40 | `D27` | DECIMAL(18,5) |  |  |  |  |
| 41 | `D28` | DECIMAL(18,5) |  |  |  |  |
| 42 | `D29` | DECIMAL(18,5) |  |  |  |  |
| 43 | `D30` | DECIMAL(18,5) |  |  |  |  |
| 44 | `D31` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCODE,
       t.WRKCENTER,
       t.RESOURCENO,
       t.ITEMTYPECODE,
       t.CODECODE,
       t.DESCCODE,
       t.FROMDATE
FROM   DB2ADMIN.WRKSTOPPAGELOSS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
