# DB2ADMIN.WRKNETCOSTSPOSTING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217542

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `EVENTCODE` | CHAR(10) |  |  |  |  |
| 5 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 7 | `CALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 8 | `CALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 9 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 13 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 14 | `COSTCENTERCODE` | CHAR(10) |  |  |  |  |
| 15 | `GLCODE` | CHAR(10) |  |  |  |  |
| 16 | `VALUE` | DECIMAL(15,5) |  |  |  |  |

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
       t.EVENTCODE,
       t.WHSACCOUNTINGGROUPCOMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.CALENDARTYPECODE,
       t.CALENDARYEAR,
       t.PERIODCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE
FROM   DB2ADMIN.WRKNETCOSTSPOSTING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
