# DB2ADMIN.PRODEMANDSALESORDERLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25149

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 2 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 3 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 7 | `LINKEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `SALESORDERCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `SALESORDERCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 10 | `ORDDLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 11 | `ORDDLVSALORDLINESALORDERCODE` | CHAR(15) |  |  |  |  |
| 12 | `ORDDLVSALESORDERLINEORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 13 | `ORDDLVSALORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 14 | `ORDDLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `ORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.COUNTERCODE,
       t.CODE,
       t.USERPRIMARYQUANTITY,
       t.USERPRIMARYUOMCODE,
       t.LINKEDQUANTITY,
       t.SALESORDERCUSTOMERTYPE,
       t.SALESORDERCUSTOMERCODE,
       t.ORDDLVSALORDLINESALORDCNTCODE,
       t.ORDDLVSALORDLINESALORDERCODE
FROM   DB2ADMIN.PRODEMANDSALESORDERLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
