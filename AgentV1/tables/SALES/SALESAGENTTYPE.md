# DB2ADMIN.SALESAGENTTYPE

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `SUBSIDIARYTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `COMPANYTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `PAYMENTLIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `INVOICELIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `COMMISSIONLIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESAGENTTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESAGENTTYPE_SALESAGENTTYPE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `SALESAGENTTYPECODE` | `AGENT.COMPANYCODE = SALESAGENTTYPE.COMPANYCODE AND AGENT.SALESAGENTTYPECODE = SALESAGENTTYPE.CODE` |
| `SALESAGENTTYPE_ENASARCODEFINITION` | [`ENASARCODEFINITION`](../SALES/ENASARCODEFINITION.md) | `SALESAGENTTYPECOMPANYCODE`, `SALESAGENTTYPECODE` | `ENASARCODEFINITION.SALESAGENTTYPECOMPANYCODE = SALESAGENTTYPE.COMPANYCODE AND ENASARCODEFINITION.SALESAGENTTYPECODE = SALESAGENTTYPE.CODE` |

## Indexes

- `SALESAGENTTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SUBSIDIARYTYPE,
       t.COMPANYTYPE,
       t.PAYMENTLIQUIDATIONTYPE,
       t.INVOICELIQUIDATIONTYPE,
       t.COMMISSIONLIQUIDATIONTYPE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.SALESAGENTTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
