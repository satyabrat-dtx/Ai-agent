# DB2ADMIN.EXTERNALDOCUMENTERRORWORK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29923

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `ORIGINCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `ORIGINCODE` | CHAR(15) |  |  |  |  |
| 7 | `ORIGINLINE` | DECIMAL(5,0) |  |  |  |  |
| 8 | `ORIGINSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `ORIGINCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `ORIGINDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `DESTINATIONDOCPROVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `DESTINATIONDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

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
       t.ORIGINTYPE,
       t.ORIGINCOUNTERCODE,
       t.ORIGINCODE,
       t.ORIGINLINE,
       t.ORIGINSUBLINE,
       t.ORIGINCOMPONENTLINE,
       t.ORIGINDELIVERYLINE,
       t.DESTINATIONDOCPROVCOUNTERCODE
FROM   DB2ADMIN.EXTERNALDOCUMENTERRORWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
