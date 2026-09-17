# DB2ADMIN.WRKCUSTINVLINEFORINVOICERPTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CREATIONTIMESTAMP`, `CUSTOMINVOICECOMPANYCODE`, `CUSTOMINVOICEDIVISIONCODE`, `CUSTOMINVOICECODE`, `INVOICELINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144604

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CUSTOMINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CUSTOMINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `CUSTOMINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `INVOICEDATE` | DATE |  |  |  |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `PRODUCTCODE` | VARCHAR(200) |  |  |  |  |
| 10 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 12 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `BOFCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `NIVCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 16 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 17 | `NUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CUSTOMINVOICECOMPANYCODE,
       t.CUSTOMINVOICEDIVISIONCODE,
       t.CUSTOMINVOICECODE,
       t.INVOICELINENO,
       t.INVOICEDATE,
       t.LONGDESCRIPTION,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.PRODUCTCODE,
       t.BASEPRIMARYQTY,
       t.BASEPRIMARYUMCODE
FROM   DB2ADMIN.WRKCUSTINVLINEFORINVOICERPTS t
FETCH FIRST 100 ROWS ONLY;
```
