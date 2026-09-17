# DB2ADMIN.CUSTOMLCLINEDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CICUSTOMINVOICEDIVISIONCODE`, `CICUSTOMINVOICECODE`, `CIINVOICELINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136587

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CICUSTOMINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CICUSTOMINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `CIINVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `LCORDERLINENO` | INTEGER | NOT NULL | FK | foreign_key |  |
| 5 | `LCORDERLCDETAILLCNO` | CHAR(35) |  | FK | foreign_key |  |
| 6 | `LCORDERLCDETAILLCDATE` | DATE |  | FK | foreign_key |  |
| 7 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `AMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LCORDERDETAIL_LCORDER` | `COMPANYCODE`, `LCORDERLINENO`, `LCORDERLCDETAILLCNO`, `LCORDERLCDETAILLCDATE` | [`LCORDERDETAIL`](../SALES/LCORDERDETAIL.md) | `COMPANYCODE`, `LINENO`, `LCDETAILLCNO`, `LCDETAILLCDATE` | RESTRICT | `CUSTOMLCLINEDETAIL.COMPANYCODE = LCORDERDETAIL.COMPANYCODE AND CUSTOMLCLINEDETAIL.LCORDERLINENO = LCORDERDETAIL.LINENO AND CUSTOMLCLINEDETAIL.LCORDERLCDETAILLCNO = LCORDERDETAIL.LCDETAILLCNO AND CUSTOMLCLINEDETAIL.LCORDERLCDETAILLCDATE = LCORDERDETAIL.LCDETAILLCDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CUSTOMLCLINEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CICUSTOMINVOICEDIVISIONCODE,
       t.CICUSTOMINVOICECODE,
       t.CIINVOICELINENO,
       t.LCORDERLINENO,
       t.LCORDERLCDETAILLCNO,
       t.LCORDERLCDETAILLCDATE,
       t.QUANTITY,
       t.AMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.CUSTOMLCLINEDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
