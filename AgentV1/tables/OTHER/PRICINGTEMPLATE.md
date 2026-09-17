# DB2ADMIN.PRICINGTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105173

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ORDERLINETEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRICINGTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRICINGTEMPLATE_TEMPLATE` | [`PRICINGDEFINITION`](../CORE_MASTER/PRICINGDEFINITION.md) | `COMPANYCODE`, `TEMPLATECODE` | `PRICINGDEFINITION.COMPANYCODE = PRICINGTEMPLATE.COMPANYCODE AND PRICINGDEFINITION.TEMPLATECODE = PRICINGTEMPLATE.CODE` |

## Indexes

- `PRICINGTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPEREQUIRED,
       t.ORDERITEMREQUIRED,
       t.DIVISIONREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.ORDERLINETEMPLATECODEREQUIRED,
       t.ORDERTEMPLATECODEREQUIRED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRICINGTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
