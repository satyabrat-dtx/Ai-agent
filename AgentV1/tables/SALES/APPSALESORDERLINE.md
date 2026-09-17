# DB2ADMIN.APPSALESORDERLINE

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `APPSALESORDERCOMPANYCODE`, `APPSALESORDERORDERID`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114305

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPSALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `APPSALESORDERORDERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINEID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `IDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `PRICE` | DECIMAL(4,1) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `UNITOFQTY` | CHAR(10) |  |  |  |  |
| 8 | `COMMENTS` | CLOB(1000000) |  |  |  |  |
| 9 | `DISCOUNT` | DECIMAL(2,0) |  |  |  |  |
| 10 | `COMMENTSIMAGE1` | BLOB(1000000) |  |  |  |  |
| 11 | `COMMENTSIMAGE2` | BLOB(1000000) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPSALESORDER_LINES` | `APPSALESORDERCOMPANYCODE`, `APPSALESORDERORDERID` | [`APPSALESORDER`](../SALES/APPSALESORDER.md) | `COMPANYCODE`, `ORDERID` | RESTRICT | `APPSALESORDERLINE.APPSALESORDERCOMPANYCODE = APPSALESORDER.COMPANYCODE AND APPSALESORDERLINE.APPSALESORDERORDERID = APPSALESORDER.ORDERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPSALESORDERLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.APPSALESORDERCOMPANYCODE,
       t.APPSALESORDERORDERID,
       t.LINEID,
       t.IDENTIFIER,
       t.ITEMTYPECODE,
       t.PRICE,
       t.QUANTITY,
       t.UNITOFQTY,
       t.COMMENTS,
       t.DISCOUNT,
       t.COMMENTSIMAGE1,
       t.COMMENTSIMAGE2
FROM   DB2ADMIN.APPSALESORDERLINE t
FETCH FIRST 100 ROWS ONLY;
```
