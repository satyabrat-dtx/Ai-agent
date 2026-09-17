# DB2ADMIN.INVOICEPREFIXDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `INVOICEPREFIXCOMPANYCODE`, `INVOICEPREFIXCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124467

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INVOICEPREFIXCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INVOICEPREFIXCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 4 | `STARTSEQUENCENO` | DECIMAL(12,0) |  |  |  |  |
| 5 | `RUNNINGSEQUENCENO` | DECIMAL(12,0) |  |  |  |  |
| 6 | `LASTINVOICEDATE` | DATE |  |  |  |  |
| 7 | `INVOICELENGTH` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INVOICEPREFIX_PREFIXDETAIL` | `INVOICEPREFIXCOMPANYCODE`, `INVOICEPREFIXCODE` | [`INVOICEPREFIX`](../OTHER/INVOICEPREFIX.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INVOICEPREFIXDETAIL.INVOICEPREFIXCOMPANYCODE = INVOICEPREFIX.COMPANYCODE AND INVOICEPREFIXDETAIL.INVOICEPREFIXCODE = INVOICEPREFIX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INVOICEPREFIXDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INVOICEPREFIXCOMPANYCODE,
       t.INVOICEPREFIXCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.STARTSEQUENCENO,
       t.RUNNINGSEQUENCENO,
       t.LASTINVOICEDATE,
       t.INVOICELENGTH,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.INVOICEPREFIXDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
