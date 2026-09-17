# DB2ADMIN.EXPENSEMRNDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `EXPUNIQUEID`, `COMPANYCODE`, `DIVISIONCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `CODE`, `INVOICEDATE`, `LINENO`, `MRNCODE`, `MRNPREFIXCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132771

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXPUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CODE` | CHAR(25) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `INVOICEDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `MRNCODE` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 9 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXPENSEMRNDETAIL.COMPANYCODE = COMPANY.CODE` |
| `ORDERPARTNER_ORDERPARTNER` | `COMPANYCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `EXPENSEMRNDETAIL.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND EXPENSEMRNDETAIL.ORDPRNCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND EXPENSEMRNDETAIL.ORDPRNCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXPENSEMRNDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXPUNIQUEID,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.CODE,
       t.INVOICEDATE,
       t.LINENO,
       t.MRNCODE,
       t.MRNPREFIXCODE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME
FROM   DB2ADMIN.EXPENSEMRNDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
