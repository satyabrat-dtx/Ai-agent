# DB2ADMIN.WRKPREWEAVINGPRODUCTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COUNTER`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131651

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `COUNTER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 9 | `PRODUCTCODE` | CHAR(100) |  |  |  |  |
| 10 | `CONTAINERITEMDETAIL` | CHAR(100) |  |  |  |  |
| 11 | `MACHINECODE` | CHAR(8) |  |  |  |  |
| 12 | `TOTALENDS` | DECIMAL(7,0) |  |  |  |  |
| 13 | `ENDDRAWN` | INTEGER | NOT NULL |  |  |  |
| 14 | `STARTTIME` | TIME |  |  |  |  |
| 15 | `PROGRESSPARTIALENDTIME` | TIME |  |  |  |  |
| 16 | `REMARKS` | CHAR(50) |  |  |  |  |
| 17 | `OPERATORCODE` | CHAR(8) |  |  |  |  |
| 18 | `OPERATOR2CODE` | CHAR(8) |  |  |  |  |
| 19 | `OPERATOR3CODE` | CHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.COUNTER,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.WORKCENTERCODE,
       t.DEMANDCOUNTERCODE,
       t.DEMANDCODE,
       t.PRODUCTCODE,
       t.CONTAINERITEMDETAIL,
       t.MACHINECODE
FROM   DB2ADMIN.WRKPREWEAVINGPRODUCTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
