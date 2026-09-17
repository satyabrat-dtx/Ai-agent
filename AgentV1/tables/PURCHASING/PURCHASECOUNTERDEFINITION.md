# DB2ADMIN.PURCHASECOUNTERDEFINITION

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8074

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `ORDERTYPE` | CHAR(1) | NOT NULL | FK | foreign_key |  |
| 3 | `DOCUMENTTYPE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 5 | `STATISTICALGROUPCODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `PURCHASETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PURCHASECOUNTERDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASECOUNTERDEFINITION.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PURCHASECOUNTERDEFINITION.COUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASECOUNTERDEFINITION.COMPANYCODE = DIVISION.COMPANYCODE AND PURCHASECOUNTERDEFINITION.DIVISIONCODE = DIVISION.CODE` |
| `DOCUMENTTYPE_DOCUMENT` | `ORDERTYPE`, `DOCUMENTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `PURCHASECOUNTERDEFINITION.ORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND PURCHASECOUNTERDEFINITION.DOCUMENTTYPE = DOCUMENTTYPE.TYPE` |
| `PURCHASEORDERTEMPLATE_PURCHASETEMPLATE` | `COMPANYCODE`, `PURCHASETEMPLATECODE` | [`PURCHASEORDERTEMPLATE`](../PURCHASING/PURCHASEORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASECOUNTERDEFINITION.COMPANYCODE = PURCHASEORDERTEMPLATE.COMPANYCODE AND PURCHASECOUNTERDEFINITION.PURCHASETEMPLATECODE = PURCHASEORDERTEMPLATE.CODE` |
| `STATISTICALGROUP_STATISTICALGROUP` | `STATISTICALGROUPCOMPANYCODE`, `STATISTICALGROUPCODE` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASECOUNTERDEFINITION.STATISTICALGROUPCOMPANYCODE = STATISTICALGROUP.COMPANYCODE AND PURCHASECOUNTERDEFINITION.STATISTICALGROUPCODE = STATISTICALGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASECOUNTERDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ORDERTYPE,
       t.DOCUMENTTYPE,
       t.DIVISIONCODE,
       t.STATISTICALGROUPCODE,
       t.PURCHASETEMPLATECODE,
       t.COUNTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.PURCHASECOUNTERDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
