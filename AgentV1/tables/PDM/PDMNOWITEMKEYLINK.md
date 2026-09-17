# DB2ADMIN.PDMNOWITEMKEYLINK

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `DBRECTYCODE`, `DBTPREC`, `DBCITEM`, `DBVERNR`, `DBVERST`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90431

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DBRECTYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `DBRECTYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DBTPREC` | DECIMAL(1,0) | NOT NULL | PK | primary_key |  |
| 4 | `DBCITEM` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `DBVERNR` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `DBVERST` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PDMNOWITEMKEYLINK.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PDMNOWITEMKEYLINK.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_DBRECTY` | `DBRECTYCOMPANYCODE`, `DBRECTYCODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMNOWITEMKEYLINK.DBRECTYCOMPANYCODE = ITEMTYPE.COMPANYCODE AND PDMNOWITEMKEYLINK.DBRECTYCODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMNOWITEMKEYLINK.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PDMNOWITEMKEYLINK.ITEMTYPEAFICODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMNOWITEMKEYLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DBRECTYCOMPANYCODE,
       t.DBRECTYCODE,
       t.DBTPREC,
       t.DBCITEM,
       t.DBVERNR,
       t.DBVERST,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.PDMNOWITEMKEYLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
