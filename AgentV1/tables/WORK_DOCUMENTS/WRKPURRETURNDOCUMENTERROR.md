# DB2ADMIN.WRKPURRETURNDOCUMENTERROR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61521

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `DLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 6 | `DLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `DLVPURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `DLVPURORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 11 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 12 | `RETURNDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 13 | `RETURNDOCUMENTLINE` | DECIMAL(7,0) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPURRETURNDOCUMENTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ORIGINTYPE,
       t.DLVPURORDLINEPURORDCNTCODE,
       t.DLVPURORDLINEPURORDERCODE,
       t.DLVPURCHASEORDERLINEORDERLINE,
       t.DLVPURORDERLINEORDERSUBLINE,
       t.DELIVERYDELIVERYLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER
FROM   DB2ADMIN.WRKPURRETURNDOCUMENTERROR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
